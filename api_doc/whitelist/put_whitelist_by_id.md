# PUT /whitelist/{whitelist_id}


Update a whitelist entry (change username or endpoint).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| whitelist_id | UUID | Whitelist entry ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | No | New username (1-100 chars) |
| erp_endpoint | string | No | New ERP endpoint |

**Response:**
```json
{
  "success": true,
  "message": "Entry updated",
  "data": { "..." : "..." }
}
```

**Errors:**
- `400` — Invalid ID or invalid endpoint
- `404` — Entry not found or would create duplicate
