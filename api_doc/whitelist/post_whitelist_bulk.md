# POST /whitelist/bulk


Bulk-create whitelist entries for a single user across multiple endpoints.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username (1-100 chars) |
| erp_endpoints | string[] | Yes | List of ERP endpoints to grant (min 1) |

**Response (201):**
```json
{
  "success": true,
  "message": "Created 3 entries, skipped 1 existing",
  "data": {
    "username": "john.doe",
    "created": ["task", "job-posts", "exercise"],
    "skipped": ["whitelist"]
  }
}
```

**Errors:**
- `400` — One or more invalid endpoints
