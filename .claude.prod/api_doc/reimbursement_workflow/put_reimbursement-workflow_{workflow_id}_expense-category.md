# PUT /reimbursement-workflow/{workflow_id}/expense-category

Update the expense category for the linked expense of an approved reimbursement. Reimbursement must be in `approved` status and expense must be in `unallocated` status. Requires `reimbursement-workflow` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | Yes | ID of the expense category to assign |

**Response:**
```json
{
  "message": "Expense category updated",
  "expense_category_id": "uuid"
}
```

**Errors:**
- `400` — Reimbursement not in `approved` status; expense not in `unallocated` status; or invalid category
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
- `404` — Reimbursement or linked expense not found
