# Timesheets API

Base prefixes:
- `/timesheets`
- `/timesheets/{workflow_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /timesheets | Authenticated employee | List Timesheets | [get_timesheets.md](get_timesheets.md) |
| POST | /timesheets/batch-create | Authenticated employee | Batch Create Timesheets | [post_timesheets_batch-create.md](post_timesheets_batch-create.md) |
| GET | /timesheets/mine | Authenticated employee | List My Timesheets | [get_timesheets_mine.md](get_timesheets_mine.md) |
| GET | /timesheets/my-team | Authenticated employee | List My Team Timesheets | [get_timesheets_my-team.md](get_timesheets_my-team.md) |
| DELETE | /timesheets/{workflow_id} | Authenticated employee | Soft Delete Timesheet | [delete_timesheets_{workflow_id}.md](delete_timesheets_{workflow_id}.md) |
| GET | /timesheets/{workflow_id} | Authenticated employee | Get Timesheet | [get_timesheets_{workflow_id}.md](get_timesheets_{workflow_id}.md) |
| POST | /timesheets/{workflow_id}/approve | Authenticated employee | Approve Timesheet | [post_timesheets_{workflow_id}_approve.md](post_timesheets_{workflow_id}_approve.md) |
| PUT | /timesheets/{workflow_id}/entries | Authenticated employee | Put Timesheet Entries | [put_timesheets_{workflow_id}_entries.md](put_timesheets_{workflow_id}_entries.md) |
| POST | /timesheets/{workflow_id}/reject | Authenticated employee | Reject Timesheet | [post_timesheets_{workflow_id}_reject.md](post_timesheets_{workflow_id}_reject.md) |
| POST | /timesheets/{workflow_id}/submit | Authenticated employee | Submit Timesheet | [post_timesheets_{workflow_id}_submit.md](post_timesheets_{workflow_id}_submit.md) |
