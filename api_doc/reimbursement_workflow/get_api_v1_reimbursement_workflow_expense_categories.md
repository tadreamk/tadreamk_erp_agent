# GET /api/v1/reimbursement-workflow/expense-categories


Get all available expense categories for classifying reimbursements.

**Access control:** Authentication required (any user).

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Travel",
    "description": "Business travel expenses",
    "created_at": "2026-01-01T00:00:00",
    "updated_at": null,
    "updated_by": null
  }
]
```

**Errors:**
- `401` -- Not authenticated
