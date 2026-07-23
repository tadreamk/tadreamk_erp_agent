# POST /timesheets/batch-create

Batch Create Timesheets. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| period_start_date | string | Yes |  |
| period_end_date | string | Yes |  |
| submission_deadline | string | No |  |
| employee_usernames | array[string] | Yes |  |

**Response:**
```json
{
  "created": [
    {
      "id": "uuid",
      "employee_username": "string",
      "employee_preferred_name": "string",
      "manager_username": "string",
      "manager_preferred_name": "string",
      "created_by_username": "string",
      "created_by_preferred_name": "string",
      "period_start_date": "date",
      "period_end_date": "date",
      "period_month": "string",
      "submission_deadline": "date",
      "hourly_rate": "string",
      "status": "string",
      "entries": [
        {
          "date": {},
          "hours": {},
          "remark": {}
        }
      ],
      "weekly_summaries": [
        {
          "week_start": {},
          "week_end": {},
          "total_hours": {}
        }
      ],
      "total_hours": "string",
      "approved_by_username": "string",
      "approved_by_preferred_name": "string",
      "approved_at": "datetime",
      "is_active": false,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "errors": [
    {
      "employee_username": "string",
      "code": "string",
      "message": "string"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
