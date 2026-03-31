# Timesheet Workflow API

Base prefix: `/timesheet-workflow`

Employee endpoints require authentication. Finance/manager endpoints require `timesheet` whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /timesheet-workflow/my-timesheets | Authenticated | Get my timesheets | [get_timesheet-workflow_my-timesheets.md](get_timesheet-workflow_my-timesheets.md) |
| GET | /timesheet-workflow/{workflow_id} | Authenticated (owner/manager/finance) | Get timesheet detail | [get_timesheet-workflow_{workflow_id}.md](get_timesheet-workflow_{workflow_id}.md) |
| PUT | /timesheet-workflow/{workflow_id}/entries | Authenticated (owner only) | Update timesheet entries | [put_timesheet-workflow_{workflow_id}_entries.md](put_timesheet-workflow_{workflow_id}_entries.md) |
| POST | /timesheet-workflow/{workflow_id}/submit | Authenticated (owner only) | Submit timesheet | [post_timesheet-workflow_{workflow_id}_submit.md](post_timesheet-workflow_{workflow_id}_submit.md) |
| POST | /timesheet-workflow/{workflow_id}/confirm | Authenticated (owner only) | Confirm payment receipt | [post_timesheet-workflow_{workflow_id}_confirm.md](post_timesheet-workflow_{workflow_id}_confirm.md) |
| GET | /timesheet-workflow/employees | `timesheet` whitelist | List hourly employees | [get_timesheet-workflow_employees.md](get_timesheet-workflow_employees.md) |
| GET | /timesheet-workflow | `timesheet` whitelist | List all timesheets | [get_timesheet-workflow.md](get_timesheet-workflow.md) |
| POST | /timesheet-workflow/batch | `timesheet` whitelist | Batch create timesheets | [post_timesheet-workflow_batch.md](post_timesheet-workflow_batch.md) |
| POST | /timesheet-workflow/{workflow_id}/approve | `timesheet` whitelist (manager) | Approve timesheet | [post_timesheet-workflow_{workflow_id}_approve.md](post_timesheet-workflow_{workflow_id}_approve.md) |
| POST | /timesheet-workflow/{workflow_id}/reject | `timesheet` whitelist (manager) | Reject timesheet | [post_timesheet-workflow_{workflow_id}_reject.md](post_timesheet-workflow_{workflow_id}_reject.md) |
| DELETE | /timesheet-workflow/{workflow_id} | `timesheet` whitelist | Delete timesheet | [delete_timesheet-workflow_{workflow_id}.md](delete_timesheet-workflow_{workflow_id}.md) |
