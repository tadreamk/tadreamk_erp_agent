---
name: erp-general-query
description: Answer questions about the TadReamk ERP system by analysing the query,
  selecting the right API endpoint(s) from api_doc, and executing them. Use when user
  asks about ERP data such as "how many employees", "show me leave requests",
  "what funding sources do we have", "list expenses", or any question that requires
  reading data from the ERP system.
---

# ERP General Query

Analyse the user's question about the TadReamk ERP system, find the right API endpoint(s) to answer it, execute them, and present the result.

The user's query is: $ARGUMENTS

If the query is empty or unclear, ask the user what they want to know about the ERP system.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.
**API base URL**: `https://api-erp.tadreamk.com/api/v1`

## Step 0: Load Token

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

## Step 1: Analyse the Query

Read the user's question and determine:
1. **Which ERP module(s)** are relevant — browse the module directories in `${CLAUDE_PLUGIN_ROOT}/api_doc/` to identify candidates.
2. **What data is needed** — is the user asking to read data, create something, update something, or delete something?

To identify the right module(s), scan the `index.md` file inside the most relevant module directory under `${CLAUDE_PLUGIN_ROOT}/api_doc/`. Each `index.md` has a summary table listing all available endpoints with their HTTP method, path, and description.

Available modules:
```
articles, bank_accounts, bank_statements, calendar, comments,
company_events, company_roles, contact_directory, customer_management,
employee_contracts, employees, equipment_management,
exercise_score_instructions, exercises, expense_categories,
expense_management, funding_opportunities, funding_sources,
funding_utilization, guide_pages, guide_quiz, health, hr_ops,
job_application_workflow, job_applications, job_posts, leave_management,
market_research, notifications, onboarding, payslip_workflow,
personal_notes, personal_particular, rachel_ai, reimbursement_workflow,
task_ai_instructions, tasks, technical_reports, templates,
timesheet_workflow, treasury, whitelist
```

## Step 2: Select API Endpoint(s)

Once you identify the relevant module(s):

1. Read the module's `index.md` from `${CLAUDE_PLUGIN_ROOT}/api_doc/<module>/index.md` to see all available endpoints.
2. Pick the endpoint(s) that best answer the user's question.
3. Read the full endpoint documentation from `${CLAUDE_PLUGIN_ROOT}/api_doc/<module>/<endpoint_file>.md` to understand the request format, query parameters, and response structure.

**Important:** If the user's question is complex and requires data from multiple endpoints or modules, plan the sequence of API calls. For example:
- "Which department has the most employees?" → fetch employees, then aggregate by department.
- "Show me Alan's leave balance and active tasks" → call leave management API + tasks API.
- "What expenses are linked to funding source X?" → call funding sources to get the ID, then call funding utilization or expense management.

## Step 3: Execute API Call(s)

Execute the selected API endpoint(s) using curl:

```bash
curl -s "<API_BASE_URL>/<endpoint_path>?<query_params>" \
  -H "Authorization: Bearer <token>"
```

For POST/PUT/PATCH requests, use a temporary JSON file to avoid shell escaping issues:
1. Write the request body to a temporary file
2. Run: `curl -s -X <METHOD> "<url>" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d @<tmp_file>`
3. Delete the temporary file after use

**Iterative execution:** If the first API call reveals that additional calls are needed to fully answer the question, make those follow-up calls. For example:
- A list endpoint returns IDs that need detail lookups
- The answer requires cross-referencing data from another module
- Pagination is needed to get all results (`page`, `limit` parameters)

Continue until you have enough data to answer the user's question completely.

## Step 4: Present Results

Format the results clearly for the user:
- Use **tables** for list data (keep columns narrow, max ~80 chars wide).
- Use **key-value format** for single-record details.
- **Summarise and highlight** the answer to the user's specific question — do not just dump raw API output.
- If the data required aggregation or calculation (counts, sums, comparisons), show the computed result prominently.
- If no data was found, say so clearly.

## Guidelines

- **Read-only by default**: Only execute GET requests unless the user explicitly asks to create, update, or delete something.
- **Confirm before writes**: If the query implies a write operation (POST/PUT/PATCH/DELETE), show the user what will be sent and ask for confirmation before executing.
- **Handle errors gracefully**: If an API returns 401, tell the user their token may be expired. If 403, they lack permissions. If 404, the resource was not found. For other errors, display the error detail.
- **Respect pagination**: If an endpoint supports `page` and `limit` parameters and the user wants all results, paginate until done (but cap at a reasonable limit like 500 records).
- **Keep it concise**: Answer the question directly. Do not explain how you found the endpoint or what API you called unless the user asks.
