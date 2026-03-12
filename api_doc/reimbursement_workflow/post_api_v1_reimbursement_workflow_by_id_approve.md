# POST /api/v1/reimbursement-workflow/{workflow_id}/approve


Head of Finance approves a reimbursement request. Requires specifying an expense category. Also auto-creates an expense record from the approved reimbursement. Only allowed when status is `submitted`.

**Access control:** Must be the assigned approver or have whitelist `reimbursement-workflow`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category | UUID | Yes | Expense category ID to classify the reimbursement |

**Request example:**
```json
{
  "expense_category": "category-uuid"
}
```

**Response:**
```json
{
  "message": "Reimbursement approved",
  "status": "approved"
}
```

**Errors:**
- `400` -- Invalid expense category
- `400` -- Cannot approve reimbursement. Current status: {status}
- `401` -- Not authenticated
- `403` -- Only the Head of Finance can approve reimbursements
- `404` -- Reimbursement workflow not found
