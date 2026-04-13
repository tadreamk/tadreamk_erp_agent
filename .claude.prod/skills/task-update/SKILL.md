---
name: task-update
description: Update an existing task by slug. Use when user says "update task",
  "change task status", "task-update", "mark task as", or "modify task".
disable-model-invocation: true
---

# Task Update

Update an existing task by slug.

This command requires a task slug and the fields to update (e.g., `/task-update documentation-607495 status to in_queue`).

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

## Step 1: Parse Input

Extract from the command argument:
- **Slug**: the task slug (first argument or identifiable slug pattern like `xxx-123456`)
- **Updates**: what to change — parse natural language into fields:
  - `status` — one of: not_started, in_queue, in_progress, blocked, request_approval, completed, cancelled
  - `priority` — one of: low, medium, high, urgent, critical
  - `title` — new title
  - `description` — new description

If the slug is missing, tell the user to provide it and stop.
If no updates are clear from the input, ask the user what they want to change using the AskUserQuestion tool with the following options:

**For status**, present these options:
- `not_started` — Not yet planned
- `in_queue` — Ready to start
- `in_progress` — Actively being worked on
- `blocked` — Waiting on something
- `request_approval` — Needs approval
- `completed` — Done
- `cancelled` — No longer needed

**For priority**, present these options:
- `low` — Low priority
- `medium` — Normal priority
- `high` — High priority
- `urgent` — Needs attention soon
- `critical` — Needs immediate attention

## Step 2: Fetch Current Task

First fetch the current task to show what will change:

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/tasks/<slug>" \
  -H "Authorization: Bearer <token>"
```

If the task is not found or access denied, display the error and stop.

## Step 3: Confirm Changes

Show the user what will change:

```
Updating task: <title> (<slug>)

Changes:
  <field>: <old value> -> <new value>
  ...

Proceed?
```

## Step 4: Update via API

```bash
curl -s -X PATCH "https://api-erp.tadreamk.com/api/v1/tasks/<slug>" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"<field>": "<value>", ...}'
```

Only send the fields that are being updated. Use a temporary JSON file if the body contains special characters.

Parse the response. If the update fails, display the error and stop.

## Step 5: Display Result

```
Task updated successfully!

Slug: <slug>
<field>: <new value>
...
URL: https://erp.tadreamk.com/tasks/<slug>
```
