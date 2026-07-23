# Job Application API

Base prefixes:
- `/job-application`
- `/job-application/admin`
- `/job-application/applications`
- `/job-application/{workflow_id}`
- `/job-application/{workflow_id}/notes`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /job-application | Authenticated | List Workflows | [get_job-application.md](get_job-application.md) |
| GET | /job-application/admin/kanban | Authenticated | Admin Kanban | [get_job-application_admin_kanban.md](get_job-application_admin_kanban.md) |
| GET | /job-application/applications/{application_id} | Authenticated | Get Application For Candidate | [get_job-application_applications_{application_id}.md](get_job-application_applications_{application_id}.md) |
| GET | /job-application/interview-calendar | Authenticated employee | Interview Calendar | [get_job-application_interview-calendar.md](get_job-application_interview-calendar.md) |
| GET | /job-application/my-applications | Authenticated | My Applications | [get_job-application_my-applications.md](get_job-application_my-applications.md) |
| GET | /job-application/my-stats | Authenticated | My Workflow Stats | [get_job-application_my-stats.md](get_job-application_my-stats.md) |
| GET | /job-application/my-workflows | Authenticated | My Workflows | [get_job-application_my-workflows.md](get_job-application_my-workflows.md) |
| GET | /job-application/staff-users | Authenticated | List Staff Users | [get_job-application_staff-users.md](get_job-application_staff-users.md) |
| GET | /job-application/stats | Authenticated | Workflow Stats | [get_job-application_stats.md](get_job-application_stats.md) |
| POST | /job-application/submit | Authenticated employee | Submit Application | [post_job-application_submit.md](post_job-application_submit.md) |
| GET | /job-application/{workflow_id} | Authenticated | Get Workflow | [get_job-application_{workflow_id}.md](get_job-application_{workflow_id}.md) |
| POST | /job-application/{workflow_id}/approve | Authenticated | Approve | [post_job-application_{workflow_id}_approve.md](post_job-application_{workflow_id}_approve.md) |
| POST | /job-application/{workflow_id}/archive | Authenticated | Archive | [post_job-application_{workflow_id}_archive.md](post_job-application_{workflow_id}_archive.md) |
| POST | /job-application/{workflow_id}/assign-exercise | Authenticated | Assign Exercise | [post_job-application_{workflow_id}_assign-exercise.md](post_job-application_{workflow_id}_assign-exercise.md) |
| PUT | /job-application/{workflow_id}/bookmark | Authenticated | Toggle Bookmark | [put_job-application_{workflow_id}_bookmark.md](put_job-application_{workflow_id}_bookmark.md) |
| PUT | /job-application/{workflow_id}/interview-accept-candidate | Authenticated employee | Interview Accept Candidate | [put_job-application_{workflow_id}_interview-accept-candidate.md](put_job-application_{workflow_id}_interview-accept-candidate.md) |
| POST | /job-application/{workflow_id}/interview-confirm | Authenticated | Interview Confirm | [post_job-application_{workflow_id}_interview-confirm.md](post_job-application_{workflow_id}_interview-confirm.md) |
| POST | /job-application/{workflow_id}/interview-finish | Authenticated | Interview Finish | [post_job-application_{workflow_id}_interview-finish.md](post_job-application_{workflow_id}_interview-finish.md) |
| POST | /job-application/{workflow_id}/interview-propose | Authenticated | Interview Propose | [post_job-application_{workflow_id}_interview-propose.md](post_job-application_{workflow_id}_interview-propose.md) |
| GET | /job-application/{workflow_id}/notes | Authenticated | List Notes | [get_job-application_{workflow_id}_notes.md](get_job-application_{workflow_id}_notes.md) |
| POST | /job-application/{workflow_id}/notes | Authenticated | Create Note | [post_job-application_{workflow_id}_notes.md](post_job-application_{workflow_id}_notes.md) |
| DELETE | /job-application/{workflow_id}/notes/{note_id} | Authenticated | Delete Note | [delete_job-application_{workflow_id}_notes_{note_id}.md](delete_job-application_{workflow_id}_notes_{note_id}.md) |
| PUT | /job-application/{workflow_id}/notes/{note_id} | Authenticated | Update Note | [put_job-application_{workflow_id}_notes_{note_id}.md](put_job-application_{workflow_id}_notes_{note_id}.md) |
| POST | /job-application/{workflow_id}/reject | Authenticated | Reject | [post_job-application_{workflow_id}_reject.md](post_job-application_{workflow_id}_reject.md) |
| POST | /job-application/{workflow_id}/score-exercise | Authenticated | Score Exercise | [post_job-application_{workflow_id}_score-exercise.md](post_job-application_{workflow_id}_score-exercise.md) |
| POST | /job-application/{workflow_id}/score-interview | Authenticated | Score Interview | [post_job-application_{workflow_id}_score-interview.md](post_job-application_{workflow_id}_score-interview.md) |
| POST | /job-application/{workflow_id}/submit-exercise | Authenticated employee | Submit Exercise | [post_job-application_{workflow_id}_submit-exercise.md](post_job-application_{workflow_id}_submit-exercise.md) |
