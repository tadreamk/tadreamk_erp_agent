# GET /employees/{employee_id}

Get a specific employee. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "username": "alice",
  "work_email": "alice@company.com",
  "manager_username": "bob",
  "contract_id": "uuid",
  "personal_particular_id": "uuid",
  "onboarding_id": "uuid",
  "created_at": "datetime",
  "updated_at": "datetime",
  "updated_by": "string",
  "is_active": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
