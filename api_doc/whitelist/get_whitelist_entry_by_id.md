# GET /whitelist/entry/{whitelist_id}


Get a single whitelist entry by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | Whitelist entry ID |

**Response:**
```json
{
  "success": true,
  "message": "Entry retrieved",
  "data": { "id": "uuid", "erp_endpoint": "task", "username": "john.doe", "..." : "..." }
}
```

**Errors:**
- `400` — Invalid ID format
- `404` — Entry not found
