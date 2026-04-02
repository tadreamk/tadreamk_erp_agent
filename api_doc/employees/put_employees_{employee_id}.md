# PUT /employees/{employee_id}

Update an employee. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Request Body:** (all fields optional)
| Field | Type | Description |
|-------|------|-------------|
| work_email | string | Work email address |
| manager_username | string | Manager's username |
| contract_id | UUID | Contract ID |
| personal_particular_id | UUID | Personal particular ID |
| username | string | Username |
| is_active | boolean | Whether employee is active |

**Response:**
```json
{
  "message": "Employee updated",
  "employee": { "...employee object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
