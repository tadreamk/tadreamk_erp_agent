# GET /reimbursement-workflow/expense-categories

Get all active expense categories. Requires authentication.

**Response:** Array of expense category objects
```json
[
  {
    "id": "uuid",
    "title": "Travel",
    "is_active": true
  }
]
```

**Errors:**
- `401` — Not authenticated
