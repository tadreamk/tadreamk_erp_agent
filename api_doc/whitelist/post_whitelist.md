# POST /whitelist/

Create a new whitelist entry granting a user access to an ERP endpoint. Requires `whitelist` admin access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| erp_endpoint | string | Yes | ERP endpoint name (must be a valid endpoint) |
| username | string | Yes | Username to grant access to |

**Response:** `201 Created`
```json
{
  "success": true,
  "message": "Whitelist entry created successfully",
  "data": {
    "id": "uuid",
    "erp_endpoint": "leave-management",
    "username": "alice"
  }
}
```

**Errors:**
- `400` — Invalid endpoint name
- `401` — Not authenticated
- `403` — Not on whitelist admin access
- `409` — User already has access to this endpoint
