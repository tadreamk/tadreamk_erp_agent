# POST /timesheet-workflow/batch

Batch create timesheets for hourly employees. Requires `timesheet` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_usernames | list[string] | Yes | List of employee usernames |
| period_month | string | Yes | Month for the timesheet (e.g., `2026-01`) |
| submission_deadline | date | No | Deadline for submission |

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
- `401` — Not authenticated
- `403` — No timesheet whitelist access
