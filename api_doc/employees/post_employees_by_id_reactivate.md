# POST /employees/{employee_id}/reactivate


Reactivate a deactivated employee.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_id | UUID | Yes | Employee unique identifier |

**Response:**
```json
{
  "message": "Employee reactivated",
  "employee": {
    "id": "uuid",
    "username": "john.doe",
    "work_email": "john.doe@company.com",
    "manager_username": "jane.smith",
    "contract_id": "uuid",
    "personal_particular_id": "uuid",
    "onboarding_id": "uuid",
    "created_at": "2025-06-01T00:00:00",
    "updated_at": "2025-12-15T00:00:00",
    "updated_by": "admin.user",
    "is_active": true
  }
}
```

**Errors:**
- `400` -- Employee is already active
- `404` -- Employee not found
