# GET /api/v1/payslip-workflow/my-payslips


Get payslips belonging to the authenticated employee. Only returns payslips at `employee_signature` or `completed` status.

**Access control:** Authentication required (any user).

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john.doe",
    "employee_name": "Doe, John",
    "payroll_month": "2026-03",
    "status": "employee_signature",
    "created_at": "2026-03-01T10:00:00",
    "signed_at": null,
    "is_active": true,
    "linked_expense_id": "expense-uuid"
  }
]
```

**Errors:**
- `401` -- Not authenticated
