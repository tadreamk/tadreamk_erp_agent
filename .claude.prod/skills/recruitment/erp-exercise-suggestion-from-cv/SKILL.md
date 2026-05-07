---
name: erp-exercise-suggestion-from-cv
description: Drafts staff-only exercise recommendations for TadReamk job-application workflows by reading each candidate cover letter and resume file, choosing one active exercise, and POSTing internal workflow notes with slug and rationale. Use when triaging submitted applicants before assign-exercise, when bulk-adding exercise suggestions from CVs, or when spawning parallel sub-agents over downloaded resumes.
disable-model-invocation: true
---

# ERP exercise suggestion from CV (TadReamk)

Produces **internal staff notes** only. For actually assigning the exercise to the candidate, use **`erp-exercise-assignment`** after notes exist.

Diagrams use the **workflow-diagram** convention (plain ` ``` ` fence, stages, People Involved).

## People Involved

- **Staff** (e.g. recruiter) — lists workflows, downloads CVs, picks exercise, posts internal notes
- **System** (ERP) — stores workflow payload (`cover_letter`, `resume_url`, applications)

## Workflow overview

```
Stage 1 - [Staff] Discover cohort
  │
  │   GET /job-applications-workflow?status=submitted (paginate limit/skip)
  │   Optional: persist snapshot under collected/ when user wants a reusable id list
  │
  ▼
Stage 2 - [Staff] Pull fields per workflow_id
  │
  │   GET /job-applications-workflow/{workflow_id}
  │   Keep: candidate_name, cover_letter, resume_url, applications[].job_title
  │
  ▼
Stage 3 - [Staff] Download resume and extract text
  │
  │   curl -sL resume_url → pypdf; DOCX mislabel try python-docx / textutil
  │   Combine with cover_letter from payload
  │
  ├──[resume_url null]──> match from cover letter only or skip until file exists
  │
  ▼
Stage 4 - [Staff] Choose one exercise from catalog
  │
  │   GET /exercises/active-list — apply fit heuristics table (single best slug)
  │
  ▼
Stage 5 - [Staff] Post internal note only
  │
  │   POST /job-applications-workflow/{workflow_id}/notes
  │   [Exercise Suggestion] + title + Slug: + Rationale
  │   Do not call assign-exercise or applicant comments unless user expands scope
  │
  ▼
Done — hand off to erp-exercise-assignment for POST /assign-exercise.
```

## Source of truth

Read `.claude.prod/api_doc/job_application_workflow/` (e.g. `get_job-applications-workflow_{workflow_id}.md`, `post_job-applications-workflow_{workflow_id}_notes.md`, `get_job-applications-workflow.md`) and `exercises/` for list semantics.

## Auth and transport

- `WEBAPP_ACCESS_TOKEN` in project `.env`.
- Prefer **`curl`** for ERP JSON when Python HTTPS fails on the host.
- Base: `https://api-erp.tadreamk.com/api/v1`

## Discover candidates

- Paginate `GET /job-applications-workflow?status=submitted&limit=100&skip=…` until a short page (adjust `status` if the user targets another stage).
- Optional: persist a snapshot under `collected/` when the user wants a reusable id list.

## Pull fields per `workflow_id`

`GET /job-applications-workflow/{workflow_id}` — keep at least:

- `candidate_name`, `cover_letter`, `resume_url`, `applications[].job_title` (signals)

## Download resumes

- `curl -sL -o <path> "<resume_url>"` — verify size (discard near-empty).
- Record `local_cv_path` next to each row in a batch JSON for sub-agents or a single runner.

## Read CV text (robust order)

1. **`pypdf`** (or equivalent) on true PDFs.
2. If the file is **DOCX** mislabeled as `.pdf`, try **`python-docx`** / unzip `word/document.xml`.
3. On macOS, **invalid PDF structure** sometimes yields text via **`textutil -convert txt`**.

Combine with **`cover_letter`** from the workflow payload for matching.

## Active exercise catalog

`GET /exercises/active-list` — for each item use **`title`**, **`slug`**, **`id`** in reasoning; the **note must carry the `slug`** (assign step maps slug → `exercise_id`).

## Fit heuristics (default bias — one exercise only)

Judge from projects, stack, coursework, and role titles; pick the **single** best fit.

| Lean | Favor slug (examples) |
|------|------------------------|
| LLM / NLP / RAG / data pipelines / media ingestion | `recruitment-exercise-llm-youtube-landscape-tracker` |
| React / TS / front-end product / UI emphasis | `ai-built-web-ui-edit-simple-graphic-objects-in-react` |
| Numerics / scientific computing / heavy math / research CS | `innovative-web-visualization-nonlinear-eigenvalue-problem-with-eigenvector-dependency-nepv-ai-assisted` |
| Backend / integrations / automation / markets or reporting tilt | `recruitment-exercise-whatsapp-bot-on-top-10-world-markets-snapshot-to-pdf` |

If two tracks tie, prefer the one best supported by **resume projects** over keywords alone.

## Post internal note (required)

`POST /job-applications-workflow/{workflow_id}/notes`

**Preferred body** (easy for downstream slug parsing):

```
[Exercise Suggestion]
Recommended exercise: <exact title from active-list>
Slug: <slug>
Rationale: <1–2 sentences tied to CV + cover letter>
```

**Alternate** (also parsed elsewhere): a line like ``Suggested recruitment exercise: `some-slug-here` `` — keep slug in backticks and matching `active-list`.

Do **not** call `assign-exercise`, `comments/job_application…`, or `comments/job_application_workflow…` unless the user explicitly expands scope.

## Parallelism

- Split id list into N batch files (e.g. round-robin): each entry `{ workflow_id, candidate_name, cover_letter, local_cv_path, … }`.
- Spawn N sub-agents: each reads PDFs + letters, posts **one note per workflow**, logs **HTTP 201** per `POST`.

## Pitfalls

- **`resume_url` null** → cannot CV-match from file; use cover letter only or skip until resume exists.
- **Stale snapshots** miss new applicants — refresh from the API before a bulk run.
- **No note → no slug** for a later bulk assign pass — ensure every targeted workflow gets a note if assignments are automated.

## Completion checks

- Every targeted `workflow_id` has a new internal note containing a valid **`slug`** present in `active-list`.
- Optional: user audit sample before `erp-exercise-assignment` runs at scale.
