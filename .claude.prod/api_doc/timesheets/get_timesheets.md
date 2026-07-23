# GET /timesheets

List Timesheets. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| period_month | string | No |  |
| employee_username | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "employee_username": "string",
      "employee_preferred_name": "string",
      "period_start_date": "date",
      "period_end_date": "date",
      "period_month": "string",
      "status": "string",
      "total_hours": "string",
      "hourly_rate": "string",
      "created_at": "datetime",
      "created_by_username": "string",
      "created_by_preferred_name": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
