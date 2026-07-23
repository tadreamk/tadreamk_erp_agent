---
name: local-update-api-doc
description: Regenerate the local .claude.prod/api_doc/ directory from fullstack_erp_v2
  OpenAPI (app.openapi()). Use when user says "update api doc", "sync api doc",
  "refresh api doc", or "api-doc-update".
model: claude-sonnet-4-6
---

# API Doc Update

Regenerate `.claude.prod/api_doc/` from **ERP v2 OpenAPI**, not by copying hand-written
v1 docs from `fullstack_erp`.

**Paths:**
- ERP v2: `/Users/chenhh/projects/fullstack_erp_v2`
- Agent: `/Users/chenhh/projects/tadreamk_erp_agent`

This command takes no arguments.

## Source of truth

`api_doc` is **generated from FastAPI OpenAPI** via `app.openapi()` on the v2 app
(`backend/run_uvicorn.py` → `create_application()`). Do **not** copy
`fullstack_erp/docs/api_doc` or `fullstack_erp_v2/docs/api_doc` (those are incomplete
or v1-shaped).

## Step 1: Dump OpenAPI from ERP v2

From `/Users/chenhh/projects/fullstack_erp_v2`, use the project `venv` and import the app
(no need to keep uvicorn running):

```bash
cd /Users/chenhh/projects/fullstack_erp_v2
./venv/bin/python << 'PY'
import json, os, sys
from pathlib import Path
os.environ.setdefault("DATABASE_URL", "postgresql://u:p@localhost/db")
os.environ.setdefault("MAIN_WEBSITE_API_URL", "http://localhost:2506/api/v1")
sys.path.insert(0, "backend")
from run_uvicorn import create_application
app = create_application()
spec = app.openapi()
Path("/tmp/erp_v2_openapi.json").write_text(json.dumps(spec))
print("paths", len(spec.get("paths", {})))
PY
```

If import fails (missing deps such as `y-py`), install via
`pip install -r backend/requirements.txt` into `venv/` first (`start_app.sh` pattern).

## Step 2: Replace agent api_doc

Run the bundled generator (preferred). It wipes and regenerates
`.claude.prod/api_doc/` from live OpenAPI + route auth introspection:

```bash
cd /Users/chenhh/projects/fullstack_erp_v2
./venv/bin/python \
  /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/scripts/generate_api_doc_from_openapi.py \
  --erp-v2 /Users/chenhh/projects/fullstack_erp_v2 \
  --out /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc
```

Or, if Step 1 already wrote `/tmp/erp_v2_openapi.json` and `/tmp/erp_v2_auth_routes.json`:

```bash
./venv/bin/python \
  /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/scripts/generate_api_doc_from_openapi.py \
  --openapi-json /tmp/erp_v2_openapi.json \
  --auth-json /tmp/erp_v2_auth_routes.json \
  --out /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc
```

Template (already implemented by the script):

- Module `index.md`: `# <Title> API`, base prefixes, table columns
  `Method | Path | Auth | Description | File`
- Per-endpoint `.md`: `# METHOD /path`, path/query/body tables, response JSON,
  errors
- Paths in docs are **without** the `/api/v1` prefix
- Includes app-level `GET /` and `GET /health` under `health/`

## Step 3: Verify

```bash
find /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc -type f | wc -l
ls /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc/
```

## Step 4: Update erp-general-query skill

Read the list of module directories from the newly generated api_doc and update the
"Available modules" block in
`/Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/skills/erp-general-query/SKILL.md`.

1. List modules: `ls /Users/chenhh/projects/tadreamk_erp_agent/.claude.prod/api_doc/`
2. Format as a comma-separated list in a fenced code block (omit non-feature dirs such
   as `misc` if present).
3. Replace the existing `Available modules:` section through the closing fence.

## Step 5: Display Results

Report the sync result:

```
API doc updated — X files across Y modules generated from fullstack_erp_v2 OpenAPI (app.openapi()).
erp-general-query skill updated with Y modules.
```
