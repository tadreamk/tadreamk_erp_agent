# DELETE /treasury/transactions/{transaction_id}

Soft delete a treasury transaction. Auto-created transactions (`expense_payment`, `funder_reimbursement`) cannot be deleted.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| transaction_id | UUID | Transaction ID |

**Response:**
```json
{
  "message": "Transaction deleted"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Cannot delete auto-created transactions |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Transaction not found |
