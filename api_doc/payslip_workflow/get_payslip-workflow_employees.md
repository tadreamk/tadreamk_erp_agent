# GET /payslip-workflow/employees

Get active employees with contract data for the batch payslip creation page. Requires `payslip` whitelist access.

**Response:** Array of employee objects
```json
[
  {
    "username": "string",
    "work_email": "string",
    "contract_type": "string",
    "monthly_salary": 10000.00
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on payslip whitelist
