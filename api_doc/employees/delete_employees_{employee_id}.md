# DELETE /employees/{employee_id}

Soft delete an employee. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Response:**
```json
{
  "message": "Employee deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
- `500` — Failed to delete employee
