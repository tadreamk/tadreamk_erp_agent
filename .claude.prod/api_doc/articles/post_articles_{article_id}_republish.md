# POST /articles/{article_id}/republish

Republish Article. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "slug": "string",
  "title": "string",
  "author": "string",
  "category": "string",
  "cover_image_url": "string",
  "read_time": 0,
  "content_by_lang": {},
  "status": "string",
  "published_at": "datetime",
  "archived_at": "datetime",
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
