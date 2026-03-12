# DELETE /expenses/{expense_id}


Soft delete an expense.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Response:**
```json
{
  "message": "Expense deleted successfully"
}
```

**Errors:**
- `404` -- Expense not found
