# GET /api/v1/reimbursement-workflow/my-reimbursements


Get reimbursements belonging to the authenticated employee with optional status filtering.

**Access control:** Authentication required (any user).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john.doe",
    "employee_name": "John Doe",
    "approval_username": "finance.head",
    "status": "submitted",
    "total_value": 1500.00,
    "expense_category_title": "Travel",
    "created_at": "2026-03-01T10:00:00",
    "updated_at": null,
    "is_active": true
  }
]
```

**Errors:**
- `401` -- Not authenticated
