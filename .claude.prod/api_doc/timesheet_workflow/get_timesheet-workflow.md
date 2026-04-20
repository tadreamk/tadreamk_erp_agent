# GET /timesheet-workflow

List all timesheets (Finance/manager view). Requires `timesheet` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| period_month | string | No | Filter by period (e.g., `2026-01`) |
| employee_username | string | No | Filter by employee |
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
      "status": "submitted",
      "total_hours": 160.0,
      "total_value": 4000.00,
      "hourly_rate": 25.00,
      "submission_deadline": "2026-01-31",
      "created_at": "datetime"
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No timesheet whitelist access
