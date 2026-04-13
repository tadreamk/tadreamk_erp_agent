---
name: task-detail
description: View task details by slug. Use when user says "task detail",
  "show task", "task info", "get task", or references a specific task slug.
---

# Task Detail

View task details by slug.

This command requires a task slug as the argument (e.g., `/task-detail documentation-607495`).

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

## Step 1: Parse Slug

Extract the task slug from the command argument. If no slug is provided, tell the user to provide one (e.g., `/task-detail documentation-607495`) and stop.

## Step 2: Fetch Task

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/tasks/<slug>" \
  -H "Authorization: Bearer <token>"
```

If the API returns an error (404, 403), display the error message and stop.

## Step 3: Display Details

Display the task in a readable format:

```
## <title>

- **Slug**: <slug>
- **Status**: <status>
- **Priority**: <priority>
- **Project**: <project title or "None">
- **Start date**: <start_date>
- **End date**: <end_date or "None">
- **Members**: <username (role), username (role), ...>
- **Created by**: <created_by> on <created_at date>
- **Updated by**: <updated_by> on <modified_at date>
- **URL**: https://erp.tadreamk.com/tasks/<slug>

### Description
<description or "No description">
```
