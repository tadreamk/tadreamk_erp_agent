# POST /admin/employee-contract


Create a new employee contract. Requires the target username as a query parameter.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Username for the contract |

**Request Body (all fields optional):**
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| candidate_title | string | No | 10 | Title (Mr, Ms, Dr, etc.) |
| candidate_last_name | string | No | 100 | Last / family name |
| candidate_first_name | string | No | 100 | First / given name |
| position | string | No | 200 | Job position title |
| work_location | string | No | 200 | Work location |
| department | string | No | 100 | Department name |
| employment_type | string | No | 50 | Employment type |
| start_date | date | No | -- | Employment start date (YYYY-MM-DD) |
| employment_end_date | date | No | -- | Employment end date (YYYY-MM-DD) |
| probation_end_date | date | No | -- | Probation end date (YYYY-MM-DD) |
| monthly_salary | decimal | No | -- | Monthly salary (>= 0) |
| living_allowance | decimal | No | -- | Living allowance (>= 0) |
| annual_leave_days | int | No | -- | Annual leave days (>= 0) |
| remote_work_days | int | No | -- | Remote work days per week (>= 0) |
| hkid | string | No | 50 | HKID number |
| address | string | No | -- | Residential address |
| mobile_no | string | No | 50 | Mobile phone number |
| employee_signature | string | No | -- | Employee signature data |
| ceo_signature | string | No | -- | CEO signature data |

**Request Example:**
```json
{
  "candidate_title": "Mr",
  "candidate_last_name": "Doe",
  "candidate_first_name": "John",
  "position": "Software Engineer",
  "department": "Engineering",
  "employment_type": "Full-time",
  "start_date": "2025-06-01",
  "monthly_salary": 35000.00,
  "annual_leave_days": 14
}
```

**Response (201):**
```json
{
  "message": "Employee contract created",
  "contract": {
    "id": "uuid",
    "username": "john.doe",
    "candidate_title": "Mr",
    "candidate_last_name": "Doe",
    "candidate_first_name": "John",
    "position": "Software Engineer",
    "work_location": null,
    "department": "Engineering",
    "employment_type": "Full-time",
    "start_date": "2025-06-01",
    "employment_end_date": null,
    "probation_end_date": null,
    "monthly_salary": 35000.00,
    "living_allowance": null,
    "annual_leave_days": 14,
    "remote_work_days": null,
    "hkid": null,
    "address": null,
    "mobile_no": null,
    "employee_signed_at": null,
    "ceo_signed_at": null,
    "created_at": "2025-05-15T00:00:00",
    "updated_at": null
  }
}
```

**Errors:**
- `400` -- Contract already exists for username. Use PUT to update.
