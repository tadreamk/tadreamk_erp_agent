# PUT /timesheet-workflow/{workflow_id}/entries

Update timesheet entries. Only the employee (owner) can edit, and only when status is `pending_submission` or `rejected`.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| timesheet_entries | list | Yes | Array of timesheet entry objects |

**Response:**
```json
{
  "id": "uuid",
  "status": "pending_submission",
  "total_hours": 160.0,
  "total_value": 4000.00,
  "timesheet_entries": []
}
```

**Errors:**
- `400` — Cannot edit entries at current status
- `401` — Not authenticated
- `403` — Only the employee can edit their timesheet entries
- `404` — Timesheet not found
