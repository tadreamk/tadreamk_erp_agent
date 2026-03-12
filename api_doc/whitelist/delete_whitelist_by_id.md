# DELETE /whitelist/{whitelist_id}


Deactivate (soft delete) a whitelist entry with audit trail.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | Whitelist entry ID |

**Response:**
```json
{
  "success": true,
  "message": "Entry deactivated",
  "data": { "..." : "..." }
}
```

**Errors:**
- `400` — Invalid ID format
- `404` — Entry not found
