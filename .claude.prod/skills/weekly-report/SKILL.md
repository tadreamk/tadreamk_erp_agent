---
name: weekly-report
description: Generate a progress report from completed tasks and upload it as a
  personal note. Use when user says "weekly report", "progress report",
  "task report", "write report", or "generate report".
---

# Weekly Report

Generate a structured progress report from completed tasks over a date range, save it locally, and upload it as a personal note.

This command takes no arguments. It automatically suggests the latest full week (Monday to Sunday) and asks the user to confirm or adjust.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.
**Username** is loaded from the `TASK_USERNAME` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token and Username

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

Load the username by reading `.env` in the current working directory and extracting the `TASK_USERNAME` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it and stop.

## Step 1: Determine Date Range and Confirm

Calculate the **latest full week** (Monday to Sunday) relative to today:
- Find the most recent Sunday (if today is Sunday, use today; otherwise go back to last Sunday).
- The start date is the Monday of that same week (6 days before that Sunday).

For example, if today is Wednesday 2026-04-15, the latest full week is Monday 2026-04-06 to Sunday 2026-04-12.

Format dates as `YYYY-MM-DD`.

**Ask the user to confirm** using the AskUserQuestion tool with two questions:

1. **Start date**: "Report starts from **2026-04-06** (Monday). Change it?" — Options: "Keep" or Other (user types a different start date).
2. **End date**: "Report ends on **2026-04-12** (Sunday). Change it?" — Options: "Keep" or Other (user types a different end date).

If the user selects "Keep" for both, proceed with the suggested range. If they provide different dates, use those instead.

## Step 2: Fetch Completed Tasks

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/tasks?status=completed&modified_after=<start_date>&modified_before=<end_date>" \
  -H "Authorization: Bearer <token>"
```

Parse the JSON response. Each task contains: `title`, `slug`, `status`, `priority`, `project` (object with `title` or null), `modified_at`, `members`.

If no tasks are found, tell the user and stop.

## Step 3: Generate Report

Build a Markdown report with the following structure:

```markdown
# Task Report: DD Mon YYYY – DD Mon YYYY

**Employee:** <full name or username>
**Period:** <start_date> to <end_date>
**Tasks completed:** <count>

---

## <Project Title> (N tasks)

### <Subcategory if applicable>
- **<Task title>** — <one-sentence description expanded from the title>

## Other Tasks (N tasks)

- **<Task title>** — <one-sentence description>

---

## Summary

<2-3 sentence summary of what was accomplished, highlighting the primary focus areas>
```

**Grouping rules:**
- Group tasks by their `project.title`. Tasks with no project go under "Other Tasks".
- Within each project group, if there are 4+ tasks, further subcategorize by theme (e.g., "New Features", "UI & UX", "Database & Infrastructure", "Documentation"). Use your judgement based on the task titles.
- Sort project groups by task count descending (largest group first). "Other Tasks" always goes last.

**Description expansion:**
- Expand each task title into a one-sentence description that explains what was done, not just what the task is called.
- If a task has `priority` of `urgent` or `critical` or `high`, append *(Priority)* at the end.

## Step 4: Save Locally

Create the directory `data/weekly_report/` if it does not exist.

Save the report to `data/weekly_report/<YYMMDD>-<YYMMDD>_task_report.md` where the two dates are the start and end of the range. For example: `data/weekly_report/260330-260413_task_report.md`.

If the file already exists, ask the user whether to overwrite or skip.

## Step 5: Upload as Personal Note

Upload the report to the ERP as a personal note:

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/personal-notes" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d @<tmp_file>
```

Build the request body as a temporary JSON file to avoid shell escaping:
```json
{
  "title": "Task Report: DD Mon YYYY – DD Mon YYYY",
  "content": "<full markdown content>",
  "category": "Work"
}
```

Delete the temporary file after upload.

## Step 6: Display Summary

```
Report saved to data/weekly_report/<filename>.md
Uploaded as personal note: <note_id>

Period: <start_date> to <end_date>
Tasks completed: <count>
Projects covered: <list of project names>
```
