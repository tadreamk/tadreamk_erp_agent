# POST /timesheet-workflow/{workflow_id}/approve

Manager approves a submitted timesheet. Only the manager can approve. Status must be `submitted`. Auto-creates a payslip workflow.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Response:**
```json
{
  "message": "Timesheet approved",
  "status": "manager_approved"
}
```

**Errors:**
- `400` — Cannot approve at current status (must be `submitted`)
- `401` — Not authenticated
- `403` — Only the manager can approve
- `404` — Timesheet not found
- `500` — Timesheet approved but payslip auto-creation failed
