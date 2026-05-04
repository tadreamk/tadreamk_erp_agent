---
name: local-erp-marketing-article-weekly-assignment
description: Assign the next 5 unchecked ERP features from data/erp_features.md as
  ERP Marketing tasks, distributed one per weekday (Mon–Fri) of the coming week. Use
  when user says "weekly assignment", "assign marketing tasks", "erp marketing weekly",
  or "local-erp-marketing-article-weekly-assignment".
model: claude-sonnet-4-6
effort: medium
---

# ERP Marketing — Weekly Task Assignment

Reads the next 5 unchecked ERP features from `data/erp_features.md`, creates one ERP Marketing task per weekday (Mon–Fri) of the coming week, and marks the features as done in the checklist.

## Step 1: Determine the Target Week

Calculate the **Monday–Friday dates** for the coming week based on today's date.

- If today is Sunday, the coming week starts tomorrow (Monday).
- If today is Monday–Friday, the coming week starts next Monday.
- Assign dates: Mon = feature 1, Tue = feature 2, Wed = feature 3, Thu = feature 4, Fri = feature 5.

## Step 2: Pick the Next 5 Unchecked Features

Read `data/erp_features.md` and collect the **first 5 unchecked items** (`- [ ]`).

Each item has the format:
```
- [ ] **Feature Name** — Description [`/path/to/feature.md`]
  - Write an article to point out the pain point...
```

Extract for each:
- Feature name (bold text)
- Feature doc path (inside backticks)

## Step 3: Load Auth Token

Load `WEBAPP_ACCESS_TOKEN` from `.env` in the current working directory. If missing, try `~/.claude/.env`. Stop and tell the user if not found.

## Step 4: Read Feature Docs

For each of the 5 features, read its feature doc (from the path extracted in Step 2).

Extract:
- **Problem** section — the pain point for SME companies
- **Solution** section — how TadReamk resolves it

## Step 5: Confirm with User

Display the planned assignments before creating:

```
Ready to assign 5 ERP Marketing tasks for week of <Mon date>–<Fri date>:

  Mon <date>: <Feature 1 name>
  Tue <date>: <Feature 2 name>
  Wed <date>: <Feature 3 name>
  Thu <date>: <Feature 4 name>
  Fri <date>: <Feature 5 name>

  Project: ERP Marketing
  Status: in_queue | Priority: low

Proceed?
```

Wait for user confirmation before continuing.

## Step 6: Create Tasks via API

For each feature, create a task using `POST /api/v1/tasks/`:

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/tasks/" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d @/tmp/task_N.json
```

**Request body fields:**
| Field | Value |
|-------|-------|
| `title` | `Write article: <Feature Name> — <Short Hook>` |
| `description` | See template below |
| `priority` | `low` |
| `status` | `in_queue` |
| `start_date` | Assigned weekday date (YYYY-MM-DD) |
| `project_id` | `14dc1cb7-1bf6-4819-be79-b16fbf77cc85` (ERP Marketing) |

**Title hook:** Derive a short, punchy subtitle from the feature's pain point (e.g., "Stop Recreating Documents from Scratch", "From Spreadsheets to One-Click Approvals").

**Description template:**
```
Write an article to point out the pain point of SME companies regarding <Feature Name>, and how this feature would resolve their issue.

Feature doc: <path/to/feature.md>

Pain Point:
<Problem section from the feature doc — 2–4 sentences>

How TadReamk Solves It:
<Solution section from the feature doc — 2–4 sentences>
```

Use Python to write each payload to a temp file (e.g., `/tmp/erp_task_N.json`) to avoid shell escaping issues, then delete after the request.

If any task creation fails (non-201 response), print the error and continue with remaining tasks.

## Step 7: Mark Features as Done

For each of the 5 features successfully created, update `data/erp_features.md`:

Change `- [ ]` to `- [x]` for the corresponding feature line.

## Step 8: Display Summary

```
Weekly assignment complete!

ERP Marketing tasks created:
  Mon <date>: <title> → <slug>
  Tue <date>: <title> → <slug>
  Wed <date>: <title> → <slug>
  Thu <date>: <title> → <slug>
  Fri <date>: <title> → <slug>

data/erp_features.md: 5 features marked as done.
```

## Notes

- The ERP Marketing project ID is `14dc1cb7-1bf6-4819-be79-b16fbf77cc85` — hardcoded, no API lookup needed.
- Valid `status` values include `not_started`, `in_queue`, `in_progress`, `completed`. Do **not** use `todo`.
- Valid `priority` values: `low`, `medium`, `high`.
- Use Python (`json.dump`) to build JSON payloads — never shell heredocs with special characters.
- The feature doc path is embedded in each checklist item inside backticks.
