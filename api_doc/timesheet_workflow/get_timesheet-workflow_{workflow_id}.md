# GET /timesheet-workflow/{workflow_id}

Get timesheet workflow details. Accessible by the employee (owner), their manager, or finance users.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "john_doe",
  "manager_username": "manager_user",
  "period_month": "2026-01",
  "status": "submitted",
  "total_hours": 160.0,
  "total_value": 4000.00,
  "hourly_rate": 25.00,
  "submission_deadline": "2026-01-31",
  "timesheet_entries": [],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view this timesheet
- `404` — Timesheet not found
