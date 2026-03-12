# PUT /employees/{employee_id}


Update an employee record. Only fields included in the request body are updated.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_id | UUID | Yes | Employee unique identifier |

**Request Body (all fields optional):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | No | Username (max 100 chars) |
| work_email | string (email) | No | Work email address |
| manager_username | string | No | Manager's username (max 100 chars) |
| is_active | bool | No | Active status |

**Request Example:**
```json
{
  "manager_username": "jane.smith",
  "work_email": "john.new@company.com"
}
```

**Response:**
```json
{
  "message": "Employee updated",
  "employee": {
    "id": "uuid",
    "username": "john.doe",
    "work_email": "john.new@company.com",
    "manager_username": "jane.smith",
    "contract_id": "uuid",
    "personal_particular_id": "uuid",
    "onboarding_id": "uuid",
    "created_at": "2025-06-01T00:00:00",
    "updated_at": "2025-07-15T00:00:00",
    "updated_by": "admin.user",
    "is_active": true
  }
}
```

**Errors:**
- `404` -- Employee not found
