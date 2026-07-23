# GET /articles/public/{slug}

Get Public Article. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string |  |

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
  "published_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
