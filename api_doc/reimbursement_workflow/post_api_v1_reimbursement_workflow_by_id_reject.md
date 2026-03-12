# POST /api/v1/reimbursement-workflow/{workflow_id}/reject


Head of Finance rejects a reimbursement request. Only allowed when status is `submitted`. Transitions status to `rejected`.

**Access control:** Must be the assigned approver or have whitelist `reimbursement-workflow`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| rejection_employee_note | string | No | Reason for rejection (added to the note field) |

**Request example:**
```json
{
  "rejection_employee_note": "Receipt is missing. Please re-submit with proper documentation."
}
```

**Response:**
```json
{
  "message": "Reimbursement rejected",
  "status": "rejected"
}
```

**Errors:**
- `400` -- Cannot approve reimbursement. Current status: {status}
- `401` -- Not authenticated
- `403` -- Only the Head of Finance can approve reimbursements
- `404` -- Reimbursement workflow not found
