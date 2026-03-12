# Job Applications API

Recruitment pipeline for job applications. Candidates submit applications with resume uploads; admins manage the pipeline via a Kanban board, assign exercises, schedule interviews, and make accept/reject decisions.

**Base URL prefix:** `/api/v1`

**Application Status Workflow (7 steps):**
1. `submitted` -- Application received
2. `exercise_assigned` -- Exercise assigned by admin
3. `exercise_submitted` -- Candidate submits exercise
4. `exercise_scored` -- Exercise scored
5. `interview_proposed` / `interview_negotiating` / `interview_confirmed` -- Interview scheduling
6. `interview_finished` -- Interview completed, awaiting decision
7. `accepted` / `rejected` -- Final decision

---

## Access Control

| Endpoint Group | Authentication | Authorization |
|----------------|----------------|---------------|
| Candidate endpoints (submit, my-applications, get by ID) | Bearer token (any authenticated user) | Owner of the application, or whitelist `job-applications` for get-by-ID |
| Admin list/stats/kanban | Bearer token + admin/moderator role | Whitelist entry for `application` section (soft check -- returns empty data if no access) |
| Admin get-by-ID, status update, exercise assignment | Bearer token + admin/moderator role | `require_admin_auth` (role = admin or moderator) |
| Admin actions (accept/reject) | Bearer token + admin/moderator role | `require_admin_auth` |
| Admin interview scheduling | Bearer token + admin/moderator role | `require_admin_auth` |

---

## 7. Job Applications (Candidate)

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `POST` | `/job-applications/submit` | Submit a new job application with resume file upload. Sends a confirmation email | [post_job_applications_submit.md](./post_job_applications_submit.md) |
| `GET` | `/job-applications/my-applications` | Get all applications submitted by the currently authenticated user. Paginated. | [get_job_applications_my_applications.md](./get_job_applications_my_applications.md) |
| `GET` | `/job-applications/{application_id}` | Get a specific application by ID. Accessible by the application owner or any use | [get_job_applications_by_id.md](./get_job_applications_by_id.md) |
| `GET` | `/job-applications/admin` | List all job applications with advanced filtering and sorting. Requires admin/mo | [get_job_applications_admin.md](./get_job_applications_admin.md) |
| `GET` | `/job-applications/admin/stats` | Get application statistics grouped by status. Returns counts for each pipeline s | [get_job_applications_admin_stats.md](./get_job_applications_admin_stats.md) |
| `GET` | `/job-applications/admin/kanban` | Get applications grouped by status columns for a Kanban board view. Optionally f | [get_job_applications_admin_kanban.md](./get_job_applications_admin_kanban.md) |
| `GET` | `/job-applications/admin/{application_id}` | Get a specific application by ID (admin/moderator only). Uses `require_admin_aut | [get_job_applications_admin_by_id.md](./get_job_applications_admin_by_id.md) |
| `PATCH` | `/job-applications/admin/{application_id}/status` | Update the status of an application. Used to manually move applications through  | [patch_job_applications_admin_by_id_status.md](./patch_job_applications_admin_by_id_status.md) |
| `PATCH` | `/job-applications/{application_id}/exercise` | Assign or unassign an exercise to an application. Sends an email notification to | [patch_job_applications_by_id_exercise.md](./patch_job_applications_by_id_exercise.md) |
| `POST` | `/job-applications/admin/{application_id}/accept` | Accept a candidate. Changes status to `accepted`, sends an acceptance email, cre | [post_job_applications_admin_by_id_accept.md](./post_job_applications_admin_by_id_accept.md) |
| `POST` | `/job-applications/admin/{application_id}/reject` | Reject a candidate with a mandatory reason. Changes status to `rejected` and sen | [post_job_applications_admin_by_id_reject.md](./post_job_applications_admin_by_id_reject.md) |
| `PATCH` | `/job-applications/{application_id}/interview-schedule-admin` | Propose interview time slots to a candidate. Updates the `interview_schedule_adm | [patch_job_applications_by_id_interview_schedule_admin.md](./patch_job_applications_by_id_interview_schedule_admin.md) |
| `PATCH` | `/job-applications/{application_id}/interview-schedule-finalize` | Finalize the interview schedule by selecting a confirmed time. Sets the `intervi | [patch_job_applications_by_id_interview_schedule_finalize.md](./patch_job_applications_by_id_interview_schedule_finalize.md) |
