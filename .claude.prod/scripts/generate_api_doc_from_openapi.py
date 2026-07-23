#!/usr/bin/env python3
"""Regenerate .claude.prod/api_doc from fullstack_erp_v2 OpenAPI."""
import argparse
import inspect
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

MODULE_RULES = [
    (r"^/articles", "articles", "Articles"),
    (r"^/audit-log", "audit_log", "Audit Log"),
    (r"^/bank-accounts|^/bank-account", "bank_accounts", "Bank Accounts"),
    (r"^/bank-statements", "bank_statements", "Bank Statements"),
    (r"^/comments", "comments", "Comments"),
    (r"^/calendar/company-events", "company_events", "Company Events"),
    (r"^/company-roles|^/company-role", "company_roles", "Company Roles"),
    (r"^/contracts|^/contract", "contracts", "Contracts"),
    (r"^/customer-requirements", "customer_requirements", "Customer Requirements"),
    (r"^/customer", "customer", "Customer"),
    (r"^/document-templates", "document_templates", "Document Templates"),
    (r"^/employees|^/employee", "employees", "Employees"),
    (r"^/equipment", "equipment", "Equipment"),
    (r"^/exercise-tags", "exercise_tags", "Exercise Tags"),
    (r"^/exercises", "exercises", "Exercises"),
    (r"^/expense-categories", "expense_categories", "Expense Categories"),
    (r"^/expenses", "expenses", "Expenses"),
    (r"^/funding-opportunities", "funding_opportunities", "Funding Opportunities"),
    (r"^/funding-sources", "funding_sources", "Funding Sources"),
    (r"^/grammar", "grammar", "Grammar"),
    (r"^/hr-ops|^/talent/hr-ops", "hr_ops", "HR Ops"),
    (r"^/hr-requests", "hr_requests", "HR Requests"),
    (r"^/job-application", "job_application", "Job Application"),
    (r"^/job-posts", "job_posts", "Job Posts"),
    (r"^/leave", "leave", "Leave"),
    (r"^/librarian", "librarian", "Librarian"),
    (r"^/market-research", "market_research", "Market Research"),
    (r"^/notifications|^/notification-settings", "notifications", "Notifications"),
    (r"^/onboarding|^/talent/onboarding", "onboarding", "Onboarding"),
    (r"^/payslips", "payslips", "Payslips"),
    (r"^/personal-note", "personal_notes", "Personal Notes"),
    (r"^/personal-particulars|^/personal-particular", "personal_particular", "Personal Particular"),
    (r"^/rachel-ai", "rachel_ai", "Rachel AI"),
    (r"^/reimbursement", "reimbursement", "Reimbursement"),
    (r"^/renewal-contract-workflow|^/talent/renewal-contract-workflow|^/talent/my-documents", "renewal_contract_workflow", "Renewal Contract Workflow"),
    (r"^/task-ai-instructions", "task_ai_instructions", "Task AI Instructions"),
    (r"^/task-projects", "task_projects", "Task Projects"),
    (r"^/tasks/recurrences", "task_recurrences", "Task Recurrences"),
    (r"^/tasks", "tasks", "Tasks"),
    (r"^/technical-reports", "technical_reports", "Technical Reports"),
    (r"^/timesheets", "timesheets", "Timesheets"),
    (r"^/user-requirements", "user_requirements", "User Requirements"),
    (r"^/whitelist", "whitelist", "Whitelist"),
]


def module_for(path: str):
    for pat, slug, title in MODULE_RULES:
        if re.search(pat, path):
            return slug, title
    return "misc", "Misc"


def strip_api(path: str) -> str:
    if path.startswith("/api/v1"):
        path = path[7:] or "/"
    return path


def filename_for(method: str, path: str) -> str:
    m = method.lower()
    trailing = path.endswith("/") and path != "/"
    p = path.strip("/")
    if not p:
        return f"{m}_root.md"
    name = p.replace("/", "_")
    if trailing:
        name = name + "_"
    return f"{m}_{name}.md"


def structural(p: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", p)


def dump_openapi(erp_v2: Path):
    sys.path.insert(0, str(erp_v2 / "backend"))
    from run_uvicorn import app
    from fastapi.routing import APIRoute, APIWebSocketRoute
    spec = app.openapi()
    auth_rows = []
    for r in app.routes:
        if isinstance(r, APIRoute):
            methods = sorted(m for m in r.methods if m not in ("HEAD", "OPTIONS"))
            try:
                src = inspect.getsource(r.endpoint)
            except Exception:
                src = ""
            wl = re.findall(r'require_whitelist\([^)]*["\']([^"\']+)["\']', src)
            needs_emp = "require_employee" in src
            needs_auth = ("require_authentication" in src) or ("require_whitelist" in src) or needs_emp
            for m in methods:
                auth_rows.append({
                    "method": m,
                    "path": r.path,
                    "whitelist": wl[0] if wl else None,
                    "employee": needs_emp,
                    "auth": needs_auth,
                    "summary": r.summary or "",
                })
        elif isinstance(r, APIWebSocketRoute):
            auth_rows.append({
                "method": "WEBSOCKET",
                "path": r.path,
                "whitelist": None,
                "employee": False,
                "auth": True,
                "summary": "",
            })
    return spec, auth_rows


def schema_type(schemas, schema, depth=0):
    if not schema or depth > 4:
        return "object"
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    if "anyOf" in schema:
        parts = []
        for s in schema["anyOf"]:
            if s.get("type") == "null":
                continue
            parts.append(schema_type(schemas, s, depth + 1))
        return "|".join(parts) if parts else "any"
    t = schema.get("type", "object")
    if t == "array":
        return f"array[{schema_type(schemas, schema.get('items', {}), depth + 1)}]"
    return t


def resolve_ref(schemas, ref):
    if not ref.startswith("#/components/schemas/"):
        return None
    return schemas.get(ref.split("/")[-1])


def flatten_props(schemas, schema, required=None, depth=0):
    if not schema or depth > 3:
        return []
    if "$ref" in schema:
        schema = resolve_ref(schemas, schema["$ref"]) or {}
    if "anyOf" in schema:
        for s in schema["anyOf"]:
            if s.get("type") == "null":
                continue
            return flatten_props(schemas, s, required, depth + 1)
    if schema.get("type") == "array":
        return flatten_props(schemas, schema.get("items", {}), None, depth + 1)
    props = schema.get("properties") or {}
    req = set(required or schema.get("required") or [])
    rows = []
    for name, prop in props.items():
        rows.append((
            name,
            schema_type(schemas, prop),
            "Yes" if name in req else "No",
            (prop.get("description") or "").replace("\n", " "),
        ))
    return rows


def example_from_schema(schemas, schema, depth=0):
    if not schema or depth > 4:
        return {}
    if "$ref" in schema:
        schema = resolve_ref(schemas, schema["$ref"]) or {}
    if "anyOf" in schema:
        for s in schema["anyOf"]:
            if s.get("type") != "null":
                return example_from_schema(schemas, s, depth + 1)
        return None
    if "example" in schema:
        return schema["example"]
    if "default" in schema and schema["default"] is not None:
        return schema["default"]
    t = schema.get("type")
    if t == "object" or ("properties" in schema):
        return {k: example_from_schema(schemas, v, depth + 1) for k, v in (schema.get("properties") or {}).items()}
    if t == "array":
        return [example_from_schema(schemas, schema.get("items", {}), depth + 1)]
    if t == "string":
        fmt = schema.get("format")
        if fmt == "uuid":
            return "uuid"
        if fmt == "date-time":
            return "datetime"
        if fmt == "date":
            return "date"
        if "enum" in schema:
            return schema["enum"][0]
        return "string"
    if t == "integer":
        return 0
    if t == "number":
        return 0.0
    if t == "boolean":
        return False
    return None


def lookup_auth(auth_map, method, path):
    for cand in (path, path + "/", path.rstrip("/") or "/"):
        row = auth_map.get((method, cand))
        if row:
            return row
    for (m, p), row in auth_map.items():
        if m == method and structural(p) == structural(path):
            return row
    return None


def auth_label(row):
    if row:
        if row.get("whitelist"):
            return f"`{row['whitelist']}` whitelist"
        if row.get("employee"):
            return "Authenticated employee"
        if row.get("auth"):
            return "Authenticated"
        return "Public"
    return "Authenticated"


def describe(op, method, path):
    s = (op.get("summary") or op.get("description") or "").strip()
    if s:
        return s.split("\n")[0][:160]
    return f"{method} {path}"


def render_endpoint(schemas, ep):
    method, path, op = ep["method"], ep["path"], ep["op"]
    auth_row = ep["auth_row"]
    lines = [f"# {method} {path}", ""]
    desc = describe(op, method, path)
    if auth_row and auth_row.get("whitelist"):
        lines.append(f"{desc}. Requires `{auth_row['whitelist']}` whitelist.")
    elif auth_row and not auth_row.get("auth"):
        lines.append(f"{desc}. Public endpoint (no auth).")
    else:
        lines.append(f"{desc}. Requires authentication.")
    lines.append("")

    params = op.get("parameters") or []
    path_params = [p for p in params if p.get("in") == "path"]
    query_params = [p for p in params if p.get("in") == "query"]
    if path_params:
        lines += ["**Path Parameters:**", "| Parameter | Type | Description |", "|-----------|------|-------------|"]
        for p in path_params:
            lines.append(f"| {p.get('name')} | {schema_type(schemas, p.get('schema') or {})} | {(p.get('description') or '').replace('|', '/')} |")
        lines.append("")
    if query_params:
        lines += ["**Query Parameters:**", "| Parameter | Type | Required | Description |", "|-----------|------|----------|-------------|"]
        for p in query_params:
            req = "Yes" if p.get("required") else "No"
            d = (p.get("description") or "").replace("|", "/").replace("\n", " ")
            lines.append(f"| {p.get('name')} | {schema_type(schemas, p.get('schema') or {})} | {req} | {d} |")
        lines.append("")

    rb = (op.get("requestBody") or {}).get("content") or {}
    if "application/json" in rb:
        schema = rb["application/json"].get("schema") or {}
        rows = flatten_props(schemas, schema)
        lines.append("**Request Body:**")
        if rows:
            lines += ["| Field | Type | Required | Description |", "|-------|------|----------|-------------|"]
            for name, typ, req, d in rows:
                lines.append(f"| {name} | {typ} | {req} | {d} |")
        else:
            lines.append(f"JSON body (`{schema_type(schemas, schema)}`).")
        lines.append("")
    elif "multipart/form-data" in rb:
        schema = rb["multipart/form-data"].get("schema") or {}
        rows = flatten_props(schemas, schema)
        lines.append("**Request Body:** `multipart/form-data`")
        if rows:
            lines += ["| Field | Type | Required | Description |", "|-------|------|----------|-------------|"]
            for name, typ, req, d in rows:
                lines.append(f"| {name} | {typ} | {req} | {d} |")
        lines.append("")

    responses = op.get("responses") or {}
    success = None
    for code in ("200", "201", "202", "204"):
        if code in responses:
            success = (code, responses[code])
            break
    lines.append("**Response:**")
    if success:
        code, resp = success
        if code == "204":
            lines.append("No content (`204`).")
        else:
            content = (resp or {}).get("content") or {}
            if "application/json" in content:
                schema = content["application/json"].get("schema") or {}
                lines.append("```json")
                lines.append(json.dumps(example_from_schema(schemas, schema), indent=2, default=str))
                lines.append("```")
            else:
                lines.append((resp or {}).get("description") or f"`{code}` success")
    else:
        lines.append("Success response.")
    lines.append("")

    err_lines = []
    for code, resp in sorted(responses.items()):
        if str(code).startswith(("4", "5")):
            err_lines.append(f"- `{code}` — {(resp or {}).get('description') or 'Error'}")
    if not err_lines and auth_row and auth_row.get("auth"):
        err_lines.append("- `401` — Not authenticated")
        if auth_row.get("whitelist"):
            err_lines.append(f"- `403` — No `{auth_row['whitelist']}` whitelist access")
        err_lines.append("- `404` — Not found")
    if err_lines:
        lines.append("**Errors:**")
        lines.extend(err_lines)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_index(title, endpoints):
    seen = set()
    eps = []
    for e in sorted(endpoints, key=lambda x: (x["path"], x["method"])):
        key = (e["method"], e["path"])
        if key in seen:
            continue
        seen.add(key)
        eps.append(e)
    prefixes = sorted({e["path"].rsplit("/", 1)[0] or e["path"] for e in eps if e["path"] not in ("/", "/health")})
    lines = [f"# {title} API", ""]
    if prefixes:
        lines.append("Base prefixes:")
        for pref in prefixes[:12]:
            lines.append(f"- `{pref if pref.startswith('/') else '/' + pref}`")
        lines.append("")
    lines.append("Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.")
    lines.append("")
    lines += ["| Method | Path | Auth | Description | File |", "|--------|------|------|-------------|------|"]
    for e in eps:
        desc = describe(e["op"], e["method"], e["path"]).replace("|", "/")
        lines.append(f"| {e['method']} | {e['path']} | {auth_label(e['auth_row'])} | {desc} | [{e['file']}]({e['file']}) |")
    lines.append("")
    return "\n".join(lines), eps


def generate(out_dir: Path, spec: dict, auth_rows: list):
    schemas = spec.get("components", {}).get("schemas", {})
    auth_map = {}
    for row in auth_rows:
        p = row["path"]
        if p.startswith("/api/v1"):
            p = p[7:] or "/"
        auth_map[(row["method"].upper(), p)] = row

    modules = defaultdict(list)
    titles = {}
    for full_path, methods in spec["paths"].items():
        path = strip_api(full_path)
        for method, op in methods.items():
            if method.startswith("x-") or method in ("parameters", "head", "options"):
                continue
            method_u = method.upper()
            if method_u in ("HEAD", "OPTIONS"):
                continue
            slug, title = module_for(path)
            titles[slug] = title
            modules[slug].append({
                "method": method_u,
                "path": path,
                "op": op,
                "auth_row": lookup_auth(auth_map, method_u, path),
                "file": filename_for(method_u, path),
            })

    for row in auth_rows:
        if row["method"] != "WEBSOCKET":
            continue
        path = row["path"]
        if path.startswith("/api/v1"):
            path = path[7:] or "/"
        path = path[:-1] if len(path) > 1 and path.endswith("/") else path
        slug, title = module_for(path)
        titles[slug] = title
        if any(e["method"] == "WEBSOCKET" and e["path"] == path for e in modules[slug]):
            continue
        modules[slug].append({
            "method": "WEBSOCKET",
            "path": path,
            "op": {"summary": f"WebSocket {path}"},
            "auth_row": row,
            "file": filename_for("websocket", path),
        })

    # Health endpoints (app root)
    titles["health"] = "Health"
    modules["health"] = [
        {"method": "GET", "path": "/", "op": {"summary": "API root"}, "auth_row": {"auth": False}, "file": "get_root.md"},
        {"method": "GET", "path": "/health", "op": {"summary": "Health check"}, "auth_row": {"auth": False}, "file": "get_health.md"},
    ]
    modules.pop("misc", None)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    total = 0
    for slug in sorted(modules):
        index_md, eps = render_index(titles.get(slug, slug), modules[slug])
        mod = out_dir / slug
        mod.mkdir()
        (mod / "index.md").write_text(index_md)
        for e in eps:
            if slug == "health":
                if e["path"] == "/":
                    (mod / e["file"]).write_text("# GET /\n\nAPI root status. Public endpoint (no auth).\n\n**Response:**\n```json\n{\n  \"message\": \"TadReamk ERP API\",\n  \"version\": \"1.0.0\",\n  \"status\": \"running\"\n}\n```\n")
                else:
                    (mod / e["file"]).write_text("# GET /health\n\nHealth check. Public endpoint (no auth).\n\n**Response:**\n```json\n{\n  \"status\": \"ok\"\n}\n```\n")
            else:
                (mod / e["file"]).write_text(render_endpoint(schemas, e))
            total += 1
        print(f"{slug}: {len(eps)}")
    print(f"TOTAL_MODULES {len(modules)}")
    print(f"TOTAL_ENDPOINTS {total}")
    return sorted(modules.keys())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--erp-v2", default="/Users/chenhh/projects/fullstack_erp_v2")
    ap.add_argument("--out", default="/Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc")
    ap.add_argument("--openapi-json", default="")
    ap.add_argument("--auth-json", default="")
    args = ap.parse_args()
    erp = Path(args.erp_v2)
    if args.openapi_json and args.auth_json:
        spec = json.loads(Path(args.openapi_json).read_text())
        auth_rows = json.loads(Path(args.auth_json).read_text())
    else:
        spec, auth_rows = dump_openapi(erp)
    modules = generate(Path(args.out), spec, auth_rows)
    print("MODULES " + ",".join(modules))


if __name__ == "__main__":
    main()
