# POST /exercise-tags/{tag_id}/restore

Restore Exercise Tag. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| tag_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "name": "string",
  "status": "string",
  "usage_count": 0,
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "updated_at": "datetime",
  "updated_by": "string"
}
```

**Errors:**
- `422` — Validation Error
