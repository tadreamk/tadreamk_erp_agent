# GET /employees/{employee_id}


Get a specific employee by ID.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_id | UUID | Yes | Employee unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "username": "john.doe",
  "work_email": "john.doe@company.com",
  "manager_username": "jane.smith",
  "contract_id": "uuid",
  "personal_particular_id": "uuid",
  "onboarding_id": "uuid",
  "created_at": "2025-06-01T00:00:00",
  "updated_at": "2025-07-01T00:00:00",
  "updated_by": "admin.user",
  "is_active": true
}
```

**Errors:**
- `404` -- Employee not found
