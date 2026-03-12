---
name: task-add
description: Upload a locally drafted task to the ERP via API. Use when user
  says "upload task", "add task", "task-add", "push task", or "submit task
  draft".
disable-model-invocation: true
---

# Task Add

Upload a locally drafted task to the ERP via API.

This command takes no arguments. It reads from draft files in `data/tasks/`.

**Auth token** is loaded automatically from the `WEBAPP_ACCESS_TOKEN` variable in `.env`.

## Step 0: Load Token

Load the auth token by reading `.env` and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, tell the user to set it in `.env` and stop.

## Step 1: Select Draft

Scan `data/tasks/` for `.md` files that contain task drafts (files with a `# ` title line and metadata like Priority, Status, etc.).

- If **no drafts found**, tell the user to run `/task-draft` first and stop.
- If **one draft found**, use it automatically.
- If **multiple drafts found**, list each draft's title and ask the user which one to upload.

## Step 2: Parse Draft

Read the selected `.md` draft file and extract:
- **Title**: from the `# <title>` heading
- **Priority**: from `- **Priority**: <value>`
- **Status**: from `- **Status**: <value>`
- **Start date**: from `- **Start date**: <value>`
- **Project ID**: from `- **Project ID**: <value>` (use `null` if "None")
- **Description**: everything under the `## Description` heading

## Step 3: Confirm with User

Display the parsed task and ask the user to confirm before uploading:

```
Ready to create task:
  Title: <title>
  Priority: <priority>
  Status: <status>
  Start date: <start_date>
  Project: <project title or "None">

Proceed?
```

## Step 4: Create Task via API

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/tasks/" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d @data/tasks/tmp_create.json
```

Build the request body as a temporary JSON file `data/tasks/tmp_create.json`:

```json
{
  "title": "<title>",
  "description": "<description>",
  "priority": "<priority>",
  "status": "<status>",
  "start_date": "<start_date>",
  "project_id": "<project_id or null>"
}
```

Use a temporary file and `curl -d @file` to avoid shell escaping issues. Delete the temp file after use.

Parse the response. If creation fails, display the error and stop.

## Step 5: Clean Up and Summary

1. Delete the temporary JSON file.
2. Display the result:

```
Task created successfully!

Slug: <slug>
Title: <title>
Priority: <priority>
Status: <status>
Project: <project title or "None">
URL: https://erp.tadreamk.com/tasks/<slug>
```

3. Ask the user if they want to delete the draft file now that it's been uploaded.
