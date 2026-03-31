# DELETE /timesheet-workflow/{workflow_id}

Soft delete a timesheet. Requires `timesheet` whitelist. Only `pending_submission` timesheets can be deleted.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Response:**
```json
{
  "message": "Timesheet deleted"
}
```

**Errors:**
- `400` — Can only delete pending timesheets
- `401` — Not authenticated
- `403` — No timesheet whitelist access
- `404` — Timesheet not found
