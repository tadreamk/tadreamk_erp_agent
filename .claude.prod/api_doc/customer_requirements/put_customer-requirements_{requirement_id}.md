# PUT /customer-requirements/{requirement_id}

Update Existing Requirement. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| requirement_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No |  |
| summary | string | No |  |
| status | string | No |  |
| share_mode | string | No |  |

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
