# GET /employee-contract/me

Get the authenticated user's employee contract data. Requires authentication.

**Response:**
```json
{
  "id": "uuid",
  "username": "alice",
  "candidate_title": "Ms.",
  "candidate_last_name": "Wong",
  "candidate_first_name": "Alice",
  "position": "Software Engineer",
  "work_location": "Hong Kong",
  "department": "Engineering",
  "employment_type": "Full-time",
  "start_date": "2024-01-01",
  "employment_end_date": null,
  "probation_end_date": "2024-04-01",
  "contract_pay_type": "monthly",
  "monthly_salary": 50000.0,
  "hourly_rate": null,
  "living_allowance": 1000.0,
  "annual_leave_days": 14,
  "remote_work_days": 2,
  "hkid": "A123456(7)",
  "address": "123 Main St, HK",
  "mobile_no": "+852 1234 5678",
  "employee_signed_at": "datetime",
  "ceo_signed_at": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee contract record not found
