# GET /employees/company-roles

Get all active company role assignments with employee names. Requires `employees` whitelist.

**Response:**
```json
{
  "roles": [
    {
      "id": "uuid",
      "username": "alice",
      "role_title": "HR Manager",
      "role_description": "string",
      "is_active": true,
      "family_name": "Wong",
      "given_name": "Alice"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
