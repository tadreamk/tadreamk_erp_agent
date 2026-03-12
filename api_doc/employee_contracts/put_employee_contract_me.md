# PUT /employee-contract/me


Update employee contract data for the authenticated user. Only fields included in the request body are updated.

**Request Body:** Same fields as POST (all optional). Only provided fields are updated.

**Request Example:**
```json
{
  "mobile_no": "+852-9999-8888",
  "address": "456 New St, Hong Kong",
  "hkid": "A1234567"
}
```

**Response:**
```json
{
  "message": "Employee contract updated",
  "employee_contract": {
    "id": "uuid",
    "username": "john.doe",
    "candidate_title": "Mr",
    "candidate_last_name": "Doe",
    "candidate_first_name": "John",
    "position": "Software Engineer",
    "work_location": "Hong Kong",
    "department": "Engineering",
    "employment_type": "Full-time",
    "start_date": "2025-06-01",
    "employment_end_date": null,
    "probation_end_date": "2025-09-01",
    "monthly_salary": 35000.00,
    "living_allowance": 2000.00,
    "annual_leave_days": 14,
    "remote_work_days": 2,
    "hkid": "A1234567",
    "address": "456 New St, Hong Kong",
    "mobile_no": "+852-9999-8888",
    "employee_signed_at": "2025-05-20T10:00:00",
    "ceo_signed_at": "2025-05-22T14:00:00",
    "created_at": "2025-05-15T00:00:00",
    "updated_at": "2025-08-01T00:00:00"
  }
}
```

**Errors:**
- `401` -- Not authenticated
- `404` -- Employee contract record not found. Use POST to create.

---

## 23. Employee Contract (Admin / HR)

Base path: `/admin/employee-contract`

**Access control:** Whitelist `employee-contracts` required for all endpoints.
