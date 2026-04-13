# GET /admin/company-roles/roles/{role_title}/users

List all users with a specific role. Requires `company-roles` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| role_title | string | The role title to query |

**Response:**
```json
{
  "usernames": ["alice", "bob"],
  "role_title": "HR Manager",
  "total": 2
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-roles whitelist access
- `404` — Role not found
