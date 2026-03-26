# DELETE /whitelist/{whitelist_id}

Deactivate (soft delete) a whitelist entry with audit trail. The entry is marked inactive rather than physically deleted. Requires `whitelist` admin access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | The whitelist entry's unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Entry deactivated",
  "data": { "...deactivated entry..." }
}
```

**Errors:**
- `400` — Invalid ID format
- `401` — Not authenticated
- `403` — Not on whitelist admin access
- `404` — Entry not found
