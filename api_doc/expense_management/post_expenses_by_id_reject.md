# POST /expenses/{expense_id}/reject

CEO rejects a payslip or reimbursement-linked expense. Cascades the rejection to the linked payslip or reimbursement workflow. Manual expenses cannot be rejected through this endpoint.

**Access:** CEO role only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Request Body:**
```json
{
  "reason": "Budget not approved for this period"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | Yes | Reason for rejection (min 1 char) |

**Response:**
```json
{
  "id": "uuid",
  "status": "rejected",
  "expense_category_name": "Personnel",
  "total_value": 50000.00,
  "rejection_reason": "Budget not approved for this period"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Can only reject payslip or reimbursement-linked expenses |
| 401 | Not authenticated |
| 403 | Only CEO can reject expenses |
| 404 | Expense not found |
