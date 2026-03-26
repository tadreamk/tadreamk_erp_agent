# GET /employees/departments

Get unique departments for filter dropdown. Requires `employees` whitelist.

**Response:**
```json
{
  "departments": ["Engineering", "Finance", "HR"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
