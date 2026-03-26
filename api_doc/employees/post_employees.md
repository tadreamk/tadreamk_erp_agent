# POST /employees

Create a new employee. Requires `employees` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| work_email | string | Yes | Work email address |
| username | string | Yes | Username |

**Response:**
```json
{
  "message": "Employee created",
  "employee": {
    "id": "uuid",
    "username": "alice",
    "work_email": "alice@company.com",
    "manager_username": null,
    "contract_id": null,
    "personal_particular_id": null,
    "onboarding_id": null,
    "created_at": "datetime",
    "updated_at": "datetime",
    "updated_by": null,
    "is_active": true
  }
}
```

**Errors:**
- `400` — Employee with this work email already exists
- `401` — Not authenticated
- `403` — No employees whitelist access
