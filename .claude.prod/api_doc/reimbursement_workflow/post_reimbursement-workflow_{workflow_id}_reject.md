# POST /reimbursement-workflow/{workflow_id}/reject

Reject a reimbursement workflow (Finance action). Sends a rejection notification to the employee. Requires `reimbursement-workflow` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| rejection_employee_note | string | No | Reason for rejection to show the employee |

**Response:**
```json
{
  "message": "Reimbursement rejected",
  "status": "rejected"
}
```

**Errors:**
- `400` — Cannot reject in current status
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
- `404` — Reimbursement not found
