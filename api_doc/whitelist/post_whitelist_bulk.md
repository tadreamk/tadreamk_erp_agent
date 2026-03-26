# POST /whitelist/bulk

Create multiple whitelist entries for a single user across multiple endpoints. Skips endpoints where the user already has access. Requires `whitelist` admin access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to grant access to |
| erp_endpoints | list[string] | Yes | List of ERP endpoint names |

**Response:** `201 Created`
```json
{
  "success": true,
  "message": "Created 3 entries, skipped 1 existing",
  "data": {
    "username": "alice",
    "created": ["leave-management", "tasks", "employees"],
    "skipped": ["expense-management"]
  }
}
```

**Errors:**
- `400` — One or more invalid endpoint names
- `401` — Not authenticated
- `403` — Not on whitelist admin access
