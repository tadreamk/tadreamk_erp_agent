---
name: erp-interview-scheduling
description: Assigns TadReamk ERP recruitment interview timeslots via job-application workflows, lists exercise_submitted or bookmarked candidates, converts HKT to UTC for API payloads, and calls interview-propose once per candidate. Use when scheduling recruitment interviews, proposing interview slots to applicants on the ERP, building Fri batch grids, or when the user mentions interview-propose or workflow interview scheduling.
---

# ERP interview scheduling (recruitment)

## When to apply

Use for **TadReamk ERP** interview planning and **single-shot** proposal to candidates: discover workflows, build a slot grid (e.g. 30-minute blocks), and call **`POST /job-applications-workflow/{workflow_id}/interview-propose`** only when appropriate.

Diagrams use the **workflow-diagram** convention.

## People Involved

- **Staff** (e.g. scheduler) — discovers workflows, builds HKT slot grid, converts to UTC, calls interview-propose once per candidate when allowed
- **System** (ERP) — stores slots, emails candidate on propose
- **Candidate** — receives proposed times (email); no API calls from this skill

## Workflow overview

```
Stage 1 - [Staff] Discover workflows
  │
  │   GET /job-applications-workflow?status=exercise_submitted (and/or bookmark=true)
  │   GET /job-applications-workflow/{workflow_id} for full profile when needed
  │
  ▼
Stage 2 - [Staff] Build slot table
  │
  │   Names, workflow_id, HKT blocks → time_slots[] as UTC ISO (+00:00)
  │   HKT = UTC+8 (e.g. 09:00 HKT → T01:00:00+00:00)
  │
  ▼
Stage 3 - [Staff] Preflight per workflow before interview-propose
  │
  │   GET /job-applications-workflow/{workflow_id}
  │
  ├──[Already interview_proposed and slots match intent]──> (flow ends; do not re-POST — duplicate emails)
  │
  └──[Safe to propose]──> POST /interview-propose {"time_slots":[...], "interview_url": optional}
  │
  │   System emails candidate with proposed slot(s)
  │
  ▼
Stage 4 - [Staff] Summarize results table for user
  │
  ▼
Done — at most one interview-propose per finalized schedule unless user asks to change slots.
```

## API reference

- Base URL: `https://api-erp.tadreamk.com/api/v1`
- Auth: `Authorization: Bearer ${WEBAPP_ACCESS_TOKEN}` (load from project `.env`; e.g. `bash -lc 'set -a && source .env && set +a && curl ...'`)
- Contracts: read `.claude.prod/api_doc/job_application_workflow/` (especially `get_job-applications-workflow.md`, `get_job-applications-workflow_{workflow_id}.md`, `post_job-applications-workflow_{workflow_id}_interview-propose.md`)

## Discovery

1. **Submitted exercise, not yet moved on:** `GET /job-applications-workflow?status=exercise_submitted&limit=100`  
   Returns `workflows[]` with `id`, `candidate_name`, `username`, `status`, `position_titles`, `updated_at`.

2. **Starred (bookmark) candidates:** `GET /job-applications-workflow?bookmark=true&limit=100`

3. **Full applicant profile (email, phone, resume, cover letter, assigned exercise, applications):** `GET /job-applications-workflow/{workflow_id}`

Note: `GET /job-applications/admin` may return empty/`No access` for some tokens; prefer workflow endpoints above.

## Times and timezones

- Send **`time_slots` as UTC** ISO datetimes (e.g. `2026-05-08T01:00:00+00:00`). Align with `put_job-applications/{id}/interview-schedule-admin` docs which specify UTC.
- **HKT = UTC+8.** Example (same calendar day): 09:00 HKT → `T01:00:00+00:00`; 14:30 HKT → `T06:30:00+00:00`.
- Request body: `{"time_slots": ["<utc-1>", ...], "interview_url": "<optional>"}` — up to 5 slots per doc.

## Propose slots to applicants (email)

`POST /job-applications-workflow/{workflow_id}/interview-propose` updates workflow state and **emails the candidate** with the proposed slot(s).

### Do not duplicate interview-propose

**Call `interview-propose` at most once per workflow for a given finalized schedule.** Re-posting the same payload (or “to resend email”) sends **duplicate emails** to applicants.

Before calling:

1. `GET /job-applications-workflow/{workflow_id}`
2. If `status` is already `interview_proposed` **`and`** `interview_schedule_admin` already matches the slot(s) you intend → **do not** call `interview-propose` again. Tell the user the ERP already holds the proposal and the first mail was triggered when it was first proposed.
3. Only call **again** when the user explicitly asks to **change** the time, correct a wrong slot, or the workflow is **not** yet in the intended proposed state.

Never add a second POST for “confirmation” or “notification retry” unless product support documents a dedicated resend endpoint.

## Suggested operational sequence

1. Pull candidates (status and/or bookmark filters).
2. Build the slot table (names, `workflow_id`, HKT window, UTC payload).
3. Optional: sort order (e.g. FIFO by `updated_at`).
4. For each workflow: preflight GET → propose only if step 2 allows (see above).
5. Summarize results table for the user; flag any workflow whose ERP slot differs from the written plan (candidate or admin may have changed it).

## Related

- Bookmarks: `PUT /job-applications-workflow/{workflow_id}/bookmark`
- Exercise grading workflow scores: `.cursor/skills/exercise-grading/SKILL.md`
