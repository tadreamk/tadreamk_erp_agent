# GET /timesheets/{workflow_id}

Get Timesheet. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string |  |

**Response:**
```json
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
      "date": "date",
      "hours": "0",
      "remark": ""
    }
  ],
  "weekly_summaries": [
    {
      "week_start": "date",
      "week_end": "date",
      "total_hours": "string"
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
```

**Errors:**
- `422` — Validation Error
