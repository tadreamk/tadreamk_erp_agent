# GET /admin/company-roles/roles

List all available role titles (distinct). Requires `company-roles` whitelist.

**Response:**
```json
{
  "roles": ["CEO", "HR Manager", "Finance Manager"],
  "total": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-roles whitelist access
