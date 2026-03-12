---
name: task-overview
description: Pull active tasks for the configured user, sorted by status
  priority. Use when user says "my tasks", "task overview", "show tasks",
  "what am I working on", or "active tasks".
---

# Task Overview

Pull active tasks for the configured user, sorted by status priority.

This command takes no arguments.

**Auth token** is loaded automatically from the `WEBAPP_ACCESS_TOKEN` variable in `.env`.
**Username** is loaded from the `TASK_USERNAME` variable in `.env`.

## Step 0: Load Token and Username

Load the auth token by reading `.env` and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, tell the user to set it in `.env` and stop.

Load the username by reading `.env` and extracting the `TASK_USERNAME` value. If the variable is missing or empty, tell the user to set it in `.env` and stop.

## Step 1: Fetch Tasks from API

Call the tasks API to get all tasks where the authenticated user is a member:

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/tasks" \
  -H "Authorization: Bearer <token>"
```

Parse the JSON response. The response has `{ tasks: [...], total: int }`.

Each task object contains:
- `title` — task title
- `slug` — URL-friendly identifier
- `status` — one of: not_started, in_queue, in_progress, blocked, request_approval, completed, cancelled
- `priority` — one of: low, medium, high, urgent, critical
- `members` — array of `{ username, role }` objects
- `project` — object with `{ title, color_code }` or null
- `start_date`, `end_date` — date strings or null

## Step 2: Filter and Sort

**Filter** tasks to only include those with status:
- `in_progress`
- `in_queue`
- `not_started`

Exclude tasks with status: completed, cancelled, blocked, request_approval.

**Sort** tasks by status priority:
1. `in_progress` (first — actively being worked on)
2. `in_queue` (second — ready to start)
3. `not_started` (third — not yet planned)

Within each status group, sort by priority: critical > urgent > high > medium > low.

## Step 3: Display Results

Display the tasks grouped by status. Tables must be narrow enough to render in a terminal (max ~80 chars wide). Use only 3 columns: #, Slug (truncate to 45 chars if needed), Priority.

```
## My Active Tasks (X total)

### In Progress (N)
| # | Slug | Priority |
|---|------|----------|
| 1 | documentation-607495 | high |

### In Queue (N)
| # | Slug | Priority |
|---|------|----------|
| 1 | remove-duplicated-job-post-workflow-327165 | high |

### Not Started (N)
- contact-internal-company-members-590317 — medium
- rachel-ai-enhancement-420198 — medium
```

Rules:
- If a status group has 0 tasks, skip that section entirely.
- Display the task `slug` (not title) in all sections.
- Use table format (3 columns only: #, Slug, Priority) for **In Progress** and **In Queue** sections.
- Truncate long slugs to 45 characters with "..." to keep tables narrow.
- Use a simple bullet list for **Not Started** section (slug — priority).
- Do NOT include a Quick Links section.
