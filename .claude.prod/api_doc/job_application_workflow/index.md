# Job Application Workflow API

Base prefix: `/job-applications-workflow`

Most endpoints require `job-applications` whitelist. Some endpoints (`my-workflows`, `my-stats`, `GET /{workflow_id}`) accept the candidate's own authentication.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /job-applications-workflow | `job-applications` whitelist | List all workflows | [get_job-applications-workflow.md](get_job-applications-workflow.md) |
| GET | /job-applications-workflow/stats | `job-applications` whitelist | Get workflow statistics | [get_job-applications-workflow_stats.md](get_job-applications-workflow_stats.md) |
| GET | /job-applications-workflow/staff-users | `job-applications` whitelist | List staff users | [get_job-applications-workflow_staff-users.md](get_job-applications-workflow_staff-users.md) |
| GET | /job-applications-workflow/my-workflows | Authenticated | Get own workflows (talent) | [get_job-applications-workflow_my-workflows.md](get_job-applications-workflow_my-workflows.md) |
| GET | /job-applications-workflow/my-stats | Authenticated | Get own workflow stats | [get_job-applications-workflow_my-stats.md](get_job-applications-workflow_my-stats.md) |
| GET | /job-applications-workflow/{workflow_id} | Authenticated (staff or owner) | Get workflow detail | [get_job-applications-workflow_{workflow_id}.md](get_job-applications-workflow_{workflow_id}.md) |
| POST | /job-applications-workflow/{workflow_id}/approve | `job-applications` whitelist | Approve candidate | [post_job-applications-workflow_{workflow_id}_approve.md](post_job-applications-workflow_{workflow_id}_approve.md) |
| POST | /job-applications-workflow/{workflow_id}/reject | `job-applications` whitelist | Reject candidate | [post_job-applications-workflow_{workflow_id}_reject.md](post_job-applications-workflow_{workflow_id}_reject.md) |
| POST | /job-applications-workflow/{workflow_id}/archive | `job-applications` whitelist | Archive workflow | [post_job-applications-workflow_{workflow_id}_archive.md](post_job-applications-workflow_{workflow_id}_archive.md) |
| PUT | /job-applications-workflow/{workflow_id}/bookmark | `job-applications` whitelist | Toggle bookmark | [put_job-applications-workflow_{workflow_id}_bookmark.md](put_job-applications-workflow_{workflow_id}_bookmark.md) |
| GET | /job-applications-workflow/{workflow_id}/notes | `job-applications` whitelist | Get workflow notes | [get_job-applications-workflow_{workflow_id}_notes.md](get_job-applications-workflow_{workflow_id}_notes.md) |
| POST | /job-applications-workflow/{workflow_id}/notes | `job-applications` whitelist | Add a note | [post_job-applications-workflow_{workflow_id}_notes.md](post_job-applications-workflow_{workflow_id}_notes.md) |
| PUT | /job-applications-workflow/{workflow_id}/notes/{note_id} | `job-applications` whitelist | Update a note | [put_job-applications-workflow_{workflow_id}_notes_{note_id}.md](put_job-applications-workflow_{workflow_id}_notes_{note_id}.md) |
| DELETE | /job-applications-workflow/{workflow_id}/notes/{note_id} | `job-applications` whitelist | Delete a note | [delete_job-applications-workflow_{workflow_id}_notes_{note_id}.md](delete_job-applications-workflow_{workflow_id}_notes_{note_id}.md) |
| POST | /job-applications-workflow/{workflow_id}/assign-exercise | `job-applications` whitelist | Assign exercise to candidate | [post_job-applications-workflow_{workflow_id}_assign-exercise.md](post_job-applications-workflow_{workflow_id}_assign-exercise.md) |
| POST | /job-applications-workflow/{workflow_id}/submit-exercise | Authenticated (owner) | Submit exercise URLs | [post_job-applications-workflow_{workflow_id}_submit-exercise.md](post_job-applications-workflow_{workflow_id}_submit-exercise.md) |
| POST | /job-applications-workflow/{workflow_id}/score-exercise | `job-applications` whitelist | Score exercise submission | [post_job-applications-workflow_{workflow_id}_score-exercise.md](post_job-applications-workflow_{workflow_id}_score-exercise.md) |
| GET | /job-applications-workflow/{workflow_id}/exercise-content | Authenticated (staff or owner) | Get exercise content | [get_job-applications-workflow_{workflow_id}_exercise-content.md](get_job-applications-workflow_{workflow_id}_exercise-content.md) |
| POST | /job-applications-workflow/{workflow_id}/interview-propose | `job-applications` whitelist | Propose interview time slots | [post_job-applications-workflow_{workflow_id}_interview-propose.md](post_job-applications-workflow_{workflow_id}_interview-propose.md) |
| POST | /job-applications-workflow/{workflow_id}/interview-accept | Authenticated (owner) | Accept interview time slot | [post_job-applications-workflow_{workflow_id}_interview-accept.md](post_job-applications-workflow_{workflow_id}_interview-accept.md) |
| POST | /job-applications-workflow/{workflow_id}/score-interview | `job-applications` whitelist | Score interview | [post_job-applications-workflow_{workflow_id}_score-interview.md](post_job-applications-workflow_{workflow_id}_score-interview.md) |
| POST | /job-applications-workflow/{workflow_id}/interview-finish | `job-applications` whitelist | Mark interview as finished | [post_job-applications-workflow_{workflow_id}_interview-finish.md](post_job-applications-workflow_{workflow_id}_interview-finish.md) |
| POST | /job-applications-workflow/{workflow_id}/interview-set-interviewers | `job-applications` whitelist | Set interviewers | [post_job-applications-workflow_{workflow_id}_interview-set-interviewers.md](post_job-applications-workflow_{workflow_id}_interview-set-interviewers.md) |
