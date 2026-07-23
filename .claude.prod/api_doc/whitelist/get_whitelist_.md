# GET /whitelist/

Get Whitelist Entries. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| erp_endpoint | string | No |  |
| username | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "string",
      "erp_endpoint": "string",
      "username": "string",
      "preferred_name": "string",
      "created_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "is_active": false,
      "updated_by": "string",
      "updated_by_preferred_name": "string",
      "updated_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
