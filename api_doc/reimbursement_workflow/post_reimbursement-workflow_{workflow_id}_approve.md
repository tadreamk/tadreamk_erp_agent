# POST /reimbursement-workflow/{workflow_id}/approve

Approve a reimbursement workflow (Finance action). Creates an unallocated expense record linked to the reimbursement. Requires `reimbursement-workflow` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:**
```json
{
  "message": "Reimbursement approved",
  "status": "approved"
}
```

**Errors:**
- `400` — Cannot approve in current status
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
- `404` — Reimbursement not found
