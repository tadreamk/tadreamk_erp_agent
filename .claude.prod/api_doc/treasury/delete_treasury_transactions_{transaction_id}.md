# DELETE /treasury/transactions/{transaction_id}

Soft delete a treasury transaction. Cannot delete auto-created transactions (`expense_payment` or `funder_reimbursement` types). Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| transaction_id | UUID | The transaction's unique identifier |

**Response:**
```json
{
  "message": "Transaction deleted"
}
```

**Errors:**
- `400` — Cannot delete auto-created transactions
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Transaction not found
