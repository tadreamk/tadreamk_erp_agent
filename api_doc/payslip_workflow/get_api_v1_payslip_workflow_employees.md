# GET /api/v1/payslip-workflow/employees


Get active employees with contract data for the batch creation page.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Response:**
```json
[
  {
    "username": "john.doe",
    "work_email": "john.doe@company.com",
    "title": "Mr",
    "family_name": "Doe",
    "given_name": "John",
    "position": "Software Engineer",
    "monthly_salary": 30000.0,
    "living_allowance": 5000.0,
    "hkid": "A1234567"
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to payslip section
