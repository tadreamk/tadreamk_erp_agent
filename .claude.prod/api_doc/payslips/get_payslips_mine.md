# GET /payslips/mine

List My Payslips. Requires authentication.

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "string",
    "employee_preferred_name": "string",
    "payroll_month": "string",
    "status": "string",
    "net_pay": "0.00",
    "created_by_username": "string",
    "created_by_preferred_name": "string",
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
