# POST /customer-requirements

Create New Requirement. Public endpoint (no auth).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Title |
| summary | string | No | Short summary |
| status | string | No | Dashboard status |
| share_mode | string | No | Public share mode |

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
