# POST /timesheet-workflow/{workflow_id}/submit

Submit timesheet for manager approval. Only the employee (owner) can submit. Status must be `pending_submission` or `rejected`.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Response:**
```json
{
  "message": "Timesheet submitted",
  "status": "submitted"
}
```

**Errors:**
- `400` — Cannot submit at current status
- `401` — Not authenticated
- `403` — Only the employee can submit their timesheet
- `404` — Timesheet not found
