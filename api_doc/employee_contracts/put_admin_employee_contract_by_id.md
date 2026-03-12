# PUT /admin/employee-contract/{contract_id}


Update an existing employee contract. Only fields included in the request body are updated.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| contract_id | string | Yes | Contract unique identifier |

**Request Body:** Same fields as POST (all optional). Only provided fields are updated.

**Request Example:**
```json
{
  "monthly_salary": 40000.00,
  "position": "Senior Software Engineer",
  "probation_end_date": "2025-09-01"
}
```

**Response:**
```json
{
  "message": "Employee contract updated",
  "contract": {
    "id": "uuid",
    "username": "john.doe",
    "candidate_title": "Mr",
    "candidate_last_name": "Doe",
    "candidate_first_name": "John",
    "position": "Senior Software Engineer",
    "work_location": "Hong Kong",
    "department": "Engineering",
    "employment_type": "Full-time",
    "start_date": "2025-06-01",
    "employment_end_date": null,
    "probation_end_date": "2025-09-01",
    "monthly_salary": 40000.00,
    "living_allowance": 2000.00,
    "annual_leave_days": 14,
    "remote_work_days": 2,
    "hkid": "A1234567",
    "address": "123 Main St, Hong Kong",
    "mobile_no": "+852-1234-5678",
    "employee_signed_at": "2025-05-20T10:00:00",
    "ceo_signed_at": "2025-05-22T14:00:00",
    "created_at": "2025-05-15T00:00:00",
    "updated_at": "2025-08-15T00:00:00"
  }
}
```

**Errors:**
- `404` -- Contract not found
