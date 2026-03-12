# POST /whitelist/


Create a new whitelist entry.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| erp_endpoint | string | Yes | ERP endpoint to grant access to |
| username | string | Yes | Username to grant access (1-100 chars) |

**Response (201):**
```json
{
  "success": true,
  "message": "Whitelist entry created successfully",
  "data": { "id": "uuid", "erp_endpoint": "task", "username": "john.doe" }
}
```

**Errors:**
- `400` — Invalid endpoint
- `409` — User already has access to this endpoint
