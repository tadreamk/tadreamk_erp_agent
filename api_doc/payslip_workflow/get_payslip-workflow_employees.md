# GET /payslip-workflow/employees

Get active employees with contract data for the batch payslip creation page. Requires `payslip` whitelist access.

**Response:** Array of employee objects
```json
[
  {
    "username": "string",
    "title": "string",
    "family_name": "string",
    "given_name": "string",
    "position": "string",
    "work_email": "string",
    "contract_pay_type": "string",
    "monthly_salary": 10000.00,
    "living_allowance": 0.00,
    "hkid": "string",
    "hourly_rate": 0.00
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on payslip whitelist
