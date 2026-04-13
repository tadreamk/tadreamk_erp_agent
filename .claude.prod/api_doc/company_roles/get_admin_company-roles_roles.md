# GET /admin/company-roles/roles

List all available role titles (distinct). Requires `company-roles` whitelist.

**Response:** `roles` is an array of objects with `title` and `description`.
```json
{
  "roles": [
    {"title": "CEO", "description": "Chief Executive Officer"},
    {"title": "HR Manager", "description": "Human Resources Manager"},
    {"title": "Finance Manager", "description": "Finance Department Manager"}
  ],
  "total": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-roles whitelist access
