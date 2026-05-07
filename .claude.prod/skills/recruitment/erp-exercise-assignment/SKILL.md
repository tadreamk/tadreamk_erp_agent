---
name: erp-exercise-assignment
description: Assigns TadReamk recruitment exercises from internal staff notes only after a mandatory pre-flight overview confirms each target workflow has a parsable exercise slug in staff notes; otherwise directs the user to run erp-exercise-suggestion-from-cv first. Verifies assignments and optionally posts applicant-facing workflow comments via curl. Use when bulk-assigning exercises, checking note coverage before assign, or troubleshooting job_application_workflow comments.
disable-model-invocation: true
---

# ERP recruitment exercise assignment (TadReamk)

Diagrams in this skill use the **workflow-diagram** convention (plain ` ``` ` fence, `Stage N - [Actor] …`, `│` / `▼` / `├──` / `└──`, People Involved first).

## People Involved

- **Staff** (e.g. recruiter) — paginates workflows, runs pre-flight, calls assign-exercise, optional applicant comments, verification
- **System** (ERP) — stores workflows, transitions status, sends exercise-assigned email

## Workflow overview

```
Stage 1 - [Staff] Optional internal exercise recommendation
  │
  │   POST /job-applications-workflow/{wf}/notes
  │   "[Exercise Suggestion]" + Slug: …  (staff-only; not visible to candidate)
  │
  ▼
Stage 2 - [Staff] Discover submitted cohort
  │
  │   GET /job-applications-workflow?status=submitted (paginate skip/limit)
  │   Optional: merge with saved JSON snapshot when the user keeps one
  │
  ▼
Stage 3 - [Staff] Pre-flight — internal-note coverage (mandatory gate)
  │
  │   Prefetch GET /exercises/active-list (valid slug set, longest match first)
  │   Per target workflow_id: GET /notes — parse slug; must be in active-list
  │
  │   If any in-scope row lacks parsable slug → (flow ends; do not bulk assign):
  │     report workflow_id, candidate_name, notes_total; tell user:
  │     run erp-exercise-suggestion-from-cv first
  │
  │   When every in-scope row has a slug:
  ▼
Stage 4 - [Staff] Per workflow_id — assign loop (after gate passes)
  │
  │   GET /job-applications-workflow/{wf}
  │
  ├──[status != submitted]──> skip (idempotent) unless user intentionally re-assigns
  │
  └──[status == submitted]──> GET /notes → slug → exercise_id from active-list
                                POST /assign-exercise {"exercise_id": "<uuid>"}
  │
  │   System: 200 → status exercise_assigned (+ email to candidate)
  │
  ▼
Stage 5 - [Staff] Optional applicant-visible comment thread
  │
  │   POST /comments/job_application_workflow/{wf}/permissions
  │   POST /comments/job_application_workflow/{wf}
  │   Do not post only to comments/job_application/{job_application_id} — UI mismatch
  │
  ▼
Stage 6 - [Staff] Verification
  │
  │   GET workflow + GET notes → exercise_id matches slug map; tally by exercise title
  │
  ▼
Done — cohort processed.

Parallelism (operational): run pre-flight on the **full** cohort first; split the **passed** workflow_id list across N sub-agents; each runs Stage 4–6 with curl only.
```

## Source of truth

Before calling the API, read relevant specs under `.claude.prod/api_doc/` (e.g. `job_application_workflow/`, `exercises/`, `comments/`).

## Auth and transport

- Load `WEBAPP_ACCESS_TOKEN` from project `.env` (and `TASK_USERNAME` if granting comment permissions).
- Prefer `curl` from a shell for JSON APIs when Python TLS to the host fails.
- Base URL: `https://api-erp.tadreamk.com/api/v1`

## Pre-flight: internal-note coverage (mandatory)

Before any `assign-exercise` call on a cohort:

1. **Define the cohort** — e.g. paginate `GET /job-applications-workflow?status=submitted` (or the user’s explicit `workflow_id` list). Only rows you intend to assign in this run count toward the check.
2. **Prefetch** `GET /exercises/active-list` and build the set of valid **`slug`** values (and longest-first ordering for substring matching).
3. **Overview pass** — for each target `workflow_id`:
   - `GET /job-applications-workflow/{workflow_id}` — if not assigning this status (e.g. already `exercise_assigned`), exclude from the *missing-recommendation* report or skip per your rules.
   - `GET /job-applications-workflow/{workflow_id}/notes` — using the same parsing rules as **Internal recommendations**, decide if at least one note yields a **slug** present in `active-list`.
4. **Gate** — if **any** row in scope still has **no** parsable recommendation:
   - **Do not** bulk `POST .../assign-exercise`.
   - Report a short table: `workflow_id`, `candidate_name`, `notes_total`, and that slug was **not** found.
   - Tell the user explicitly: run **`erp-exercise-suggestion-from-cv`** (attach that skill) to add staff internal notes with a valid slug, then return to this skill.

Proceed only when every in-scope **submitted** (or user-targeted) workflow has a parsable slug, unless the user clearly overrides the gate for named exceptions.

## Recommended exercise list

- `GET /exercises/active-list` returns `{ exercises: [{ id, title, slug }, ...] }`.
- Assignment body needs **`exercise_id` (UUID)**, not slug: `POST /job-applications-workflow/{workflow_id}/assign-exercise` with `{"exercise_id":"<uuid>"}`.

## Internal recommendations (staff-only)

- Staff notes: `GET` / `POST /job-applications-workflow/{workflow_id}/notes` (not visible to candidates per docs).
- Common note shapes to support when parsing:
  - `[Exercise Suggestion]` block with a line `Slug: recruitment-exercise-...`
  - `` `slug-in-backticks` `` (batch_2 style)
  - Substring match against known active `slug` values (longest slug first if ambiguous).

## Assignment loop (idempotent)

Run only after **Pre-flight: internal-note coverage** passes (or user-named exceptions).

For each target `workflow_id`:

1. `GET /job-applications-workflow/{workflow_id}` — if status is not `submitted`, skip unless you intentionally re-assign (normally stop at `exercise_assigned`).
2. `GET /job-applications-workflow/{workflow_id}/notes` — derive **slug** from the exercise-suggestion note (same rules as pre-flight).
3. Map slug → UUID via cached `active-list`.
4. `POST /job-applications-workflow/{workflow_id}/assign-exercise` with `{"exercise_id": uuid}`.
5. Expect **200** and workflow moves to **`exercise_assigned`** (response may include `new_status`).

Do **not** run git commit/push/pull unless the user explicitly allows it.

## Optional: sub-agents for scale

- Either run **pre-flight once** on all ids, then distribute only **cleared** ids into batches, **or** have each sub-agent report missing slugs upward and stop until the parent confirms coverage.
- Split workflow id list into **4 (or N) batches** (e.g. round-robin by index).
- Each sub-agent: same assign loop as above using **curl only**, no comments unless asked.
- Skip documenting duplicate confirmations to the user.

## Applicant-facing “comment session” (if needed)

The UI thread for candidates is tied to **`job_application_workflow`**, not `job_application`.

1. `POST /comments/job_application_workflow/{workflow_id}/permissions` body `{"username":"<TASK_USERNAME>"}` (201).
2. `POST /comments/job_application_workflow/{workflow_id}` body `{"content":"..."}` (201).

Posting only to `comments/job_application/{job_application_id}` can succeed in the API but **not appear** in the applicant UI. Remove misplaced rows with `DELETE /comments/{comment_id}` if you created them by mistake.

## Verification

For a cohort of `workflow_id` values:

- Every workflow should be `exercise_assigned` (or later if your process advances them).
- Re-parse slug from notes and confirm `detail.exercise_id` equals `active-list` mapping.
- Summarize counts by **`exercise_id`** / title (distribution report).

## Operational pitfalls

- **Stale JSON snapshots** (e.g. `collected/job_applications/workflows_submitted.json`) omit **new** `submitted` workflows; refresh with paginated `GET /job-applications-workflow?status=submitted` before bulk runs.
- **No parsable recommendation in internal notes** → **pre-flight fails** → stop and point the user to **`erp-exercise-suggestion-from-cv`** (do not silently skip assign for those rows in a bulk run unless the user overrides).
- **Pagination**: list endpoints may use `limit` / `skip`; exhaust pages until a short page is returned.

## Data collection helper (optional)

To refresh a merged snapshot: paginate `status=submitted`, then per id `GET /job-applications-workflow/{id}` for contact, applications[], earliest `applied_at`, and write one JSON file under `collected/` only when the user wants a saved artifact.
