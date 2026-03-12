# DELETE /employees/{employee_id}


Soft-delete an employee record.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_id | UUID | Yes | Employee unique identifier |

**Response:**
```json
{
  "message": "Employee deleted successfully"
}
```

**Errors:**
- `404` -- Employee not found
- `500` -- Failed to delete employee
