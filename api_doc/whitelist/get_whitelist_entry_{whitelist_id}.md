# GET /whitelist/entry/{whitelist_id}

Get a single whitelist entry by ID. Requires `whitelist` admin access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | The whitelist entry's unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Entry retrieved",
  "data": {
    "id": "uuid",
    "erp_endpoint": "leave-management",
    "username": "alice",
    "is_active": true
  }
}
```

**Errors:**
- `400` — Invalid ID format
- `401` — Not authenticated
- `403` — Not on whitelist admin access
- `404` — Entry not found
