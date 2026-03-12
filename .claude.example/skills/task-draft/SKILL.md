---
name: task-draft
description: Create a local task draft for review before uploading. Use when
  user says "draft task", "create task draft", "task-draft", "new task", or
  "plan a task".
disable-model-invocation: true
---

# Task Draft

Create a local task draft for review before uploading.

This command requires user input describing the task (title, what it's about, etc.).

**Username** is loaded from the `TASK_USERNAME` variable in `.env` — this user will be the **manager** of the task.

## Step 0: Load Username

Load the username by reading `.env` and extracting the `TASK_USERNAME` value. If the variable is missing or empty, tell the user to set it in `.env` and stop.

## Step 1: Parse User Input

From the user's input (provided as the command argument), determine:
- **Title**: A concise task title (max 500 chars)
- **Description**: A brief summary sentence followed by bullet points breaking down key items, subtasks, or requirements. If the user gives a short input, expand it into a summary + bullet points.
- **Priority**: One of `low`, `medium`, `high`, `urgent`, `critical`. Default to `medium` unless the user indicates urgency.

## Step 2: Ask for Project

Ask the user which project this task belongs to. Fetch the active projects list:

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/task-projects/active-list" \
  -H "Authorization: Bearer <token>"
```

Load the auth token from `WEBAPP_ACCESS_TOKEN` in `.env` for this call.

Present the projects as options for the user to pick from, plus a "None" option for no project.

## Step 3: Save Draft

Generate a slug from the title: lowercase, replace spaces and special chars with hyphens, remove consecutive hyphens, trim to reasonable length. Prefix with `{YYMMDD}_{HHMM}_` using the current date and time. Example: "Create a list of commands" at 2026-03-04 15:30 becomes `260304_1530_create-a-list-of-commands`.

Create a Markdown draft file at `data/tasks/<YYMMDD_HHMM_slug>.md` with:

```markdown
# <title>

- **Priority**: <priority>
- **Status**: in_queue
- **Start date**: <today's date YYYY-MM-DD>
- **Project**: <project title or "None">
- **Project ID**: <project id or "None">
- **Manager**: <TASK_USERNAME from .env>

## Description

<brief summary sentence>

- <key item or subtask>
- <key item or subtask>
- ...
```

Create the `data/tasks/` directory if it doesn't exist.

If `data/tasks/<YYMMDD_HHMM_slug>.md` already exists, ask the user whether to overwrite or save as `<YYMMDD_HHMM_slug>_<N>.md` (increment N).

## Step 4: Display Summary

Show the draft summary:

```
Task draft saved to data/tasks/<YYMMDD_HHMM_slug>.md

Title: <title>
Priority: <priority>
Project: <project title or "None">
Manager: <TASK_USERNAME>

To upload this task, run /task-add
```
