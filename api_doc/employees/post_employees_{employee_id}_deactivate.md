# POST /employees/{employee_id}/deactivate

Deactivate an employee. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Response:**
```json
{
  "message": "Employee deactivated",
  "employee": { "...employee object..." }
}
```

**Errors:**
- `400` — Employee is already deactivated
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
