# POST /employees/{employee_id}/reactivate

Reactivate a deactivated employee. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Response:**
```json
{
  "message": "Employee reactivated",
  "employee": { "...employee object..." }
}
```

**Errors:**
- `400` — Employee is already active
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
