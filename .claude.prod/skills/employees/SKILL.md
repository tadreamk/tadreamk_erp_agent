---
name: employees
description: List all employees from the ERP system. Use when user says "list
  employees", "show employees", "all employees", "employee list", or "who works here".
---

# Employees

List all employees from the ERP system with optional filtering.

This command accepts optional arguments:
- A search term (e.g., `/employees alan`)
- `--inactive` flag to include inactive employees (e.g., `/employees --inactive`)
- `--department <name>` to filter by department (e.g., `/employees --department Engineering`)

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

## Step 1: Parse Arguments

Extract optional arguments from the command:
- If a plain text argument is provided, use it as the `search` query parameter.
- If `--inactive` is present, set `include_inactive=true`.
- If `--department <name>` is present, set `department=<name>`.

## Step 2: Fetch Employees from API

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/employees?limit=100&search=<search>&include_inactive=<bool>&department=<dept>" \
  -H "Authorization: Bearer <token>"
```

Only include query parameters that were provided. The response has `{ employees: [...], total: int, page: int, limit: int }`.

Each employee object contains:
- `id` — UUID
- `username` — login name
- `work_email` — email address
- `manager_username` — manager's username or null
- `is_active` — boolean
- `created_at` — timestamp
- `full_name` — from contract (may be null)
- `position` — job title from contract (may be null)
- `department` — department from contract (may be null)
- `start_date` — employment start date from contract (may be null)

If the API returns an error, display the error message and stop.

## Step 3: Display Results

Display employees in a table. Use only these columns: #, Username, Email, Manager, Active.

```
## Employees (X total)

| # | Username | Email | Manager | Active |
|---|----------|-------|---------|--------|
| 1 | alan | alannguyen@tadreamk.com | — | Yes |
| 2 | AlexCHEN | chunhang.chen@tadreamk.com | alan | Yes |
```

Rules:
- Sort alphabetically by username.
- Show "Yes" or "No" for the Active column.
- Show "—" if manager_username is null.
- If `full_name` is available, append it in parentheses after the username: `alan (NGUYEN Alan)`.
- If `position` and `department` are available, add Position and Department columns.
- If no employees are found, display "No employees found."
