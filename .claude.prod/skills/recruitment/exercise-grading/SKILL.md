---
name: exercise-grading
description: Grades technical recruitment exercise submissions against the ERP exercise brief, runs local verification, scores 0–100 with deduction reasons, optionally posts scores to the job-applications workflow API, and writes a report under the candidate folder. Use when grading candidate exercise repos, scoring LLM take-home work, updating exercise marks in the ERP, or when the user asks for exercise grading or recruitment exercise review.
---

# Exercise grading

## When to apply

Use this skill for **recruitment / technical exercises** stored in `candidate_exercise/<Candidate>/` (or similar) where the canonical brief lives in **TadReamk ERP** (`api_doc` + live `GET /exercises/{slug}`), and scores are recorded via **`POST /job-applications-workflow/{workflow_id}/score-exercise`**.

## Workflow

### 1. Load the brief

- Read `api_doc/exercises/` (e.g. `get_exercises_{slug}.md`, `index.md`) for the **API contract** (`title`, `tags`, `content` markdown).
- If credentials allow, call `GET https://api-erp.tadreamk.com/api/v1/exercises/{slug}` (or `active-list`) for the **authoritative** `content` text. The repo does not mirror the full brief.

Extract **numbered deliverables** and any **assessment** instructions; use them as the rubric checklist.

### 2. Inspect the submission

Under the candidate folder, review the submitted code (often a subfolder repo clone):

- Entry points: `README.md`, main scripts, `requirements.txt` / lockfiles.
- Data and UI: generated JSON/CSV, static `index.html`, client search/sort.
- Automation: `.github/workflows/*.yml` (schedules, secrets, commit/push scope).
- Written report: `report.md` if present.

Note **mismatches** between report and code (model names, APIs, features claimed vs implemented).

### 3. Verification (run locally)

Execute or simulate checks appropriate to the stack:

- **Python:** `python3 -m py_compile` on main modules.
- **Data:** Load JSON; confirm required fields exist; sample rows for **invalid URLs**, nulls, or schema drift.
- **Front-end:** Grep or read for crash paths (e.g. `array.some` without guarding undefined).
- **CI:** Read workflow for duplicate steps, missing env, paths that never update the public artifact.

Record **concrete** findings (file:line when possible).

### 4. Score 0–100

- Start from **100** and **subtract** with a **short reason per deduction** (correctness, spec gaps, robustness, docs/ops).
- Weight **user-visible bugs** (e.g. broken links for a “public demo” exercise) heavily when the brief stresses live review.
- Call out **partial** credit when a deliverable is met in spirit but not in an explicit form (e.g. “how X relate” only as a flat list).
- Map **1–5** ERP scores only as a rough band if needed; the product uses integers on `score-exercise`.

### 5. ERP (optional)

If `WEBAPP_ACCESS_TOKEN` (or project `.env`) is available and the user wants the system updated:

1. Resolve **workflow_id**: `GET /api/v1/job-applications-workflow?search=<name fragment>&limit=50` and match `candidate_name`.
2. **POST** `/api/v1/job-applications-workflow/{workflow_id}/score-exercise` with JSON body:
   - `score` (integer 1–5, required)
   - `note_content` (string; must be non-empty if the API enforces minimum length)

Use `Content-Type: application/json` and `Authorization: Bearer <token>`.

### 6. Candidate summary comment (≈100 words)

Produce a **single ~100-word comment** synthesizing:

- **CV signals:** relevant experience, stack familiarity, education, prior projects (read any CV/resume file in the candidate folder if present; otherwise note "no CV on file").
- **Position applied for:** (e.g. "Long Term Internship", role text from `*.txt` markers in the candidate folder or ERP workflow). Calibrate expectations to the role seniority.
- **Exercise performance:** overall score, 1–2 biggest strengths, 1–2 biggest deductions, and hire-readiness signal.

Write in neutral, professional English. Include it as a **"Reviewer comment"** section in `exercise_grading_report.md`, and reuse it as the `note_content` body when posting to the ERP `score-exercise` endpoint.

### 7. Internal discussion notes (optional)

If the user wants the ERP workflow updated for reviewer collaboration, post to **`POST /job-applications-workflow/{workflow_id}/notes`**:

- The **reviewer comment** from Step 6 as an internal discussion note.
- A **second internal discussion note** with **2-3 proposed interview questions** tailored to the candidate's CV, target role, and specific exercise weaknesses.

When internal discussion is requested, include **both** notes by default: the reviewer comment **and** the interview-question note. Keep internal notes concise, professional, and directly grounded in evidence from the submission and CV / recruitment workflow.

### 8. Interview questions (optional)

When asked, propose **2-3 interview questions** that:

- test the candidate's understanding of the strongest or weakest parts of the submission,
- connect to the **role applied for** and relevant CV signals,
- probe debugging, research thinking, reproducibility, trade-offs, or product judgment.

When internal discussion is requested, always post these questions to the workflow internal discussion as a separate note.

### 9. Deliverables

- Write **`exercise_grading_report.md`** in the **candidate’s folder** (same level as their exercise subfolder), including: overall **0–100**, **conclusion**, **strengths**, **deduction table**, **minimal fixes**, ERP reference if used.
- If the project requires it, append a short entry to `docs/change_log/<user>/YYYY-MM-DD.md` (under 100 words per project rules).

## Report template

Use this structure for `exercise_grading_report.md`:

```markdown
# Technical exercise grading report

**Candidate:** …
**Exercise:** …
**Source brief:** ERP slug / endpoint
**Repository reviewed:** …

## Overall score: NN / 100

**Conclusion:** (2–4 sentences)

## Strengths
- …

## Score deductions (reasons)
| Area | Points | Details |
|------|--------|---------|
| … | −N | … |

## Recommended minimal fixes (priority order)
1. …

## Mapping to ERP (reference)
…
```

## Principles

- **Spec first:** Grade against the **published** `content`, not against an assumed standard take-home.
- **Evidence:** Tie deductions to files, data samples, or failed checks.
- **Minimal fixes:** Prefer small, ordered changes over rewriting the solution.
- **Security:** Do not echo bearer tokens or paste full `.env` into reports.

## api_doc pointers

- Exercises module: `api_doc/exercises/`
- Score exercise: `api_doc/job_application_workflow/post_job-applications-workflow_{workflow_id}_score-exercise.md`
- List workflows: `api_doc/job_application_workflow/get_job-applications-workflow.md`
