# PUT /whitelist/{whitelist_id}

Update a whitelist entry (change username or endpoint). Requires `whitelist` admin access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | The whitelist entry's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | No | New username |
| erp_endpoint | string | No | New ERP endpoint name |

**Response:**
```json
{
  "success": true,
  "message": "Entry updated",
  "data": { "...updated entry..." }
}
```

**Errors:**
- `400` — Invalid ID format or invalid endpoint name
- `401` — Not authenticated
- `403` — Not on whitelist admin access
- `404` — Entry not found or would create a duplicate
