# Job Applications API

Public/candidate prefix: `/job-applications` (requires authentication)
Admin prefix: `/job-applications/admin` (requires `job-applications` whitelist or admin/moderator)

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| POST | /job-applications/submit | Authenticated | Submit a job application | [post_job-applications_submit.md](post_job-applications_submit.md) |
| GET | /job-applications/my-applications | Authenticated | Get own applications | [get_job-applications_my-applications.md](get_job-applications_my-applications.md) |
| GET | /job-applications/{application_id} | Authenticated (owner or admin) | Get application by ID | [get_job-applications_{application_id}.md](get_job-applications_{application_id}.md) |
| PATCH | /job-applications/{application_id}/exercise-urls | Authenticated | Submit exercise URLs | [patch_job-applications_{application_id}_exercise-urls.md](patch_job-applications_{application_id}_exercise-urls.md) |
| GET | /job-applications/admin | `job-applications` whitelist | List all applications (admin) | [get_job-applications_admin.md](get_job-applications_admin.md) |
| GET | /job-applications/admin/stats | `job-applications` whitelist | Get application statistics | [get_job-applications_admin_stats.md](get_job-applications_admin_stats.md) |
| GET | /job-applications/admin/kanban | `job-applications` whitelist | Get Kanban board view | [get_job-applications_admin_kanban.md](get_job-applications_admin_kanban.md) |
| GET | /job-applications/admin/{application_id} | Admin/Moderator | Get application by ID (admin) | [get_job-applications_admin_{application_id}.md](get_job-applications_admin_{application_id}.md) |
| PATCH | /job-applications/admin/{application_id}/status | Admin/Moderator | Update application status | [patch_job-applications_admin_{application_id}_status.md](patch_job-applications_admin_{application_id}_status.md) |
| PATCH | /job-applications/{application_id}/exercise | Admin/Moderator | Assign exercise to application | [patch_job-applications_{application_id}_exercise.md](patch_job-applications_{application_id}_exercise.md) |
| POST | /job-applications/admin/{application_id}/accept | Admin/Moderator | Accept application | [post_job-applications_admin_{application_id}_accept.md](post_job-applications_admin_{application_id}_accept.md) |
| POST | /job-applications/admin/{application_id}/reject | Admin/Moderator | Reject application | [post_job-applications_admin_{application_id}_reject.md](post_job-applications_admin_{application_id}_reject.md) |
| PATCH | /job-applications/{application_id}/interview-schedule-admin | Admin/Moderator | Set interview schedule | [patch_job-applications_{application_id}_interview-schedule-admin.md](patch_job-applications_{application_id}_interview-schedule-admin.md) |
| PATCH | /job-applications/{application_id}/interview-schedule-finalize | Admin/Moderator | Finalize interview schedule | [patch_job-applications_{application_id}_interview-schedule-finalize.md](patch_job-applications_{application_id}_interview-schedule-finalize.md) |
