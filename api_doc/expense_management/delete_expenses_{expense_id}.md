# DELETE /expenses/{expense_id}

Soft delete an expense. Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Response:**
```json
{
  "message": "Expense deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Expense not found
