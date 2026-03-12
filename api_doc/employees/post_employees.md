# POST /employees


Create a new employee record.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| work_email | string (email) | Yes | Employee work email address |
| username | string | No | Username (max 100 chars) |

**Request Example:**
```json
{
  "work_email": "john.doe@company.com",
  "username": "john.doe"
}
```

**Response (201):**
```json
{
  "message": "Employee created",
  "employee": {
    "id": "uuid",
    "username": "john.doe",
    "work_email": "john.doe@company.com",
    "manager_username": null,
    "contract_id": null,
    "personal_particular_id": null,
    "onboarding_id": null,
    "created_at": "2025-06-01T00:00:00",
    "updated_at": null,
    "updated_by": null,
    "is_active": true
  }
}
```

**Errors:**
- `400` -- Employee with this work email already exists
