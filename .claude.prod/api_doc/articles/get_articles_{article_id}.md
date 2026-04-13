# GET /articles/{article_id}

Get a single article by its UUID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | The article's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "slug": "string",
  "summary": "string",
  "content": "string",
  "category": "string",
  "status": "draft|published",
  "author": "string",
  "cover_image_url": "string|null",
  "read_time": 5,
  "translations": {},
  "created_by": "string",
  "updated_by": "string|null",
  "publish_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
- `404` — Article not found
