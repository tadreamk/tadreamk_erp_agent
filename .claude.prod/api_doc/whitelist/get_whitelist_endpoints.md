# GET /whitelist/endpoints

Get the list of valid ERP endpoint names from the database. Requires `whitelist` admin access.

**Response:**
```json
{
  "endpoints": [
    "leave-management",
    "tasks",
    "expense-management",
    "employees"
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on whitelist admin access
