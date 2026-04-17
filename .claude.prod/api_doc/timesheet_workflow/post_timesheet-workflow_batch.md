# POST /timesheet-workflow/batch

Batch create timesheets for hourly employees. Requires `timesheet` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_usernames | list[string] | Yes | List of employee usernames |
| period_month | string | No | Month for the timesheet (e.g., `2026-01`). Derived from `period_start_date` if omitted. |
| period_start_date | date | No | Custom period start date (defaults to first of `period_month`) |
| period_end_date | date | No | Custom period end date (defaults to last of `period_month`) |
| submission_deadline | date | No | Deadline for submission |

> If `period_start_date` and `period_end_date` are omitted, they default to the first and last day of `period_month`. If `period_start_date` is provided, `period_month` is derived from it. Either `period_month` or `period_start_date` must be provided. Cross-month ranges (e.g., Mar 16 – Apr 15) are supported.

**Response:**
```json
{
  "created_count": 5,
  "timesheet_ids": ["uuid1", "uuid2"],
  "skipped": ["user1 (no hourly contract)", "user2 (already exists)"],
  "message": "Created 5 timesheets, skipped 2"
}
```

**Errors:**
- `400` — Missing required fields, or `period_end_date` before `period_start_date`
- `401` — Not authenticated
- `403` — No timesheet whitelist access
