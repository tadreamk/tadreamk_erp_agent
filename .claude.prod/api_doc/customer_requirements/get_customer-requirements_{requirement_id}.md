# GET /customer-requirements/{requirement_id}

Get Requirement. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| requirement_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "share_token": "string",
  "title": "string",
  "summary": "string",
  "status": "string",
  "share_mode": "string",
  "created_by": "string",
  "is_active": false,
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
