# Job Application Workflow API

Recruitment workflow system covering the full hiring pipeline: dashboard management, internal notes, exercise assignment/submission/scoring, interview scheduling/scoring, and final decision (approve/reject/archive).

**Base Path:** `/job-applications-workflow`

**Workflow Statuses (in order):**
1. `submitted` — Application received
2. `exercise_assigned` — Exercise assigned to candidate
3. `exercise_submitted` — Candidate submitted exercise
4. `exercise_scored` — Exercise scored by staff
5. `interview_proposed` — Interview time slots proposed
6. `interview_negotiating` — Candidate negotiating time
7. `interview_confirmed` — Interview time confirmed
8. `interview_finished` — Interview completed
9. `accepted` — Candidate approved
10. `rejected` — Candidate rejected
11. `archived` — Workflow archived

---

## Access Control

| Access Level | Description | Endpoints |
|---|---|---|
| **Whitelist (`job-applications`)** | Staff users added to the `job-applications` whitelist. Required for all dashboard, scoring, decision, and note endpoints. | Most endpoints below |
| **Authenticated (any user)** | Any logged-in user. Used for talent-facing endpoints where ownership is verified. | `my-workflows`, `my-stats`, `submit-exercise`, `interview-accept`, `exercise-content` (owner), `GET /{workflow_id}` (owner) |

All endpoints require a valid session/auth token via the `Authorization` header or session cookie.

---

## 11. Job Application Notes

Internal staff-only notes attached to a workflow. Notes are **not** visible to talent/candidates. Only the note author can update or delete their own notes. Changes are broadcast via WebSocket (`note_update` event).

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/job-applications-workflow/{workflow_id}/notes` | List all notes for a workflow. | [get_job_applications_workflow_by_id_notes.md](./get_job_applications_workflow_by_id_notes.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/notes` | Create a new note on a workflow. Optionally mention other staff users (triggers  | [post_job_applications_workflow_by_id_notes.md](./post_job_applications_workflow_by_id_notes.md) |
| `PUT` | `/job-applications-workflow/{workflow_id}/notes/{note_id}` | Update a note. Only the original author can update. | [put_job_applications_workflow_by_id_notes_by_id.md](./put_job_applications_workflow_by_id_notes_by_id.md) |
| `DELETE` | `/job-applications-workflow/{workflow_id}/notes/{note_id}` | Delete a note. Only the original author can delete. | [delete_job_applications_workflow_by_id_notes_by_id.md](./delete_job_applications_workflow_by_id_notes_by_id.md) |
| `GET` | `/job-applications-workflow` | List workflows for the dashboard with filters and pagination. | [get_job_applications_workflow.md](./get_job_applications_workflow.md) |
| `GET` | `/job-applications-workflow/stats` | Get workflow counts grouped by status. | [get_job_applications_workflow_stats.md](./get_job_applications_workflow_stats.md) |
| `GET` | `/job-applications-workflow/staff-users` | List usernames that have `job-applications` whitelist access. Used for @mention  | [get_job_applications_workflow_staff_users.md](./get_job_applications_workflow_staff_users.md) |
| `GET` | `/job-applications-workflow/my-workflows` | List workflows belonging to the authenticated user (talent/candidate view). | [get_job_applications_workflow_my_workflows.md](./get_job_applications_workflow_my_workflows.md) |
| `GET` | `/job-applications-workflow/my-stats` | Get workflow statistics for the authenticated user (talent/candidate view). | [get_job_applications_workflow_my_stats.md](./get_job_applications_workflow_my_stats.md) |
| `GET` | `/job-applications-workflow/{workflow_id}` | Get full workflow detail including applicant info, applied positions, exercise f | [get_job_applications_workflow_by_id.md](./get_job_applications_workflow_by_id.md) |
| `PATCH` | `/job-applications-workflow/{workflow_id}/bookmark` | Toggle the bookmark flag on a workflow. | [patch_job_applications_workflow_by_id_bookmark.md](./patch_job_applications_workflow_by_id_bookmark.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/approve` | Approve a candidate for a specific position. Creates an onboarding workflow with | [post_job_applications_workflow_by_id_approve.md](./post_job_applications_workflow_by_id_approve.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/reject` | Reject a candidate. Sends a rejection email to the candidate with CC to `head_of | [post_job_applications_workflow_by_id_reject.md](./post_job_applications_workflow_by_id_reject.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/archive` | Archive a workflow. No notifications are sent. | [post_job_applications_workflow_by_id_archive.md](./post_job_applications_workflow_by_id_archive.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/assign-exercise` | Assign an exercise to a candidate's workflow. Sends an email notification to the | [post_job_applications_workflow_by_id_assign_exercise.md](./post_job_applications_workflow_by_id_assign_exercise.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/submit-exercise` | Submit exercise solution URLs. Only the candidate who owns the workflow can subm | [post_job_applications_workflow_by_id_submit_exercise.md](./post_job_applications_workflow_by_id_submit_exercise.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/score-exercise` | Score an exercise submission. Optionally attach a feedback note. | [post_job_applications_workflow_by_id_score_exercise.md](./post_job_applications_workflow_by_id_score_exercise.md) |
| `GET` | `/job-applications-workflow/{workflow_id}/exercise-content` | Get the exercise content assigned to a workflow. Accessible by the workflow owne | [get_job_applications_workflow_by_id_exercise_content.md](./get_job_applications_workflow_by_id_exercise_content.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/interview-propose` | Propose interview time slots to the candidate. Sends an email to the candidate w | [post_job_applications_workflow_by_id_interview_propose.md](./post_job_applications_workflow_by_id_interview_propose.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/interview-accept` | Accept one of the proposed interview time slots. Only the candidate who owns the | [post_job_applications_workflow_by_id_interview_accept.md](./post_job_applications_workflow_by_id_interview_accept.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/score-interview` | Score a completed interview. Optionally attach a feedback note. | [post_job_applications_workflow_by_id_score_interview.md](./post_job_applications_workflow_by_id_score_interview.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/interview-finish` | Mark an interview as finished. | [post_job_applications_workflow_by_id_interview_finish.md](./post_job_applications_workflow_by_id_interview_finish.md) |
| `POST` | `/job-applications-workflow/{workflow_id}/interview-set-interviewers` | Set or update the list of interviewers for a workflow. | [post_job_applications_workflow_by_id_interview_set_interviewers.md](./post_job_applications_workflow_by_id_interview_set_interviewers.md) |
