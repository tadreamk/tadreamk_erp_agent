# GET /timesheet-workflow/my-timesheets

Get timesheets for the authenticated user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status (pending_submission, submitted, manager_approved, paid, confirmed, rejected) |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "timesheets": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "employee_name": "John Doe",
      "period_month": "2026-01",
      "status": "pending_submission",
      "total_hours": 160.0,
      "total_value": 4000.00,
      "hourly_rate": 25.00,
      "submission_deadline": "2026-01-31",
      "created_at": "datetime"
    }
  ],
  "total": 10,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
