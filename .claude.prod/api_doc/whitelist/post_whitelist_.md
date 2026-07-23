# POST /whitelist/

Create Whitelist Entry. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| erp_endpoint | string | Yes |  |
| username | string | Yes |  |

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `422` — Validation Error
