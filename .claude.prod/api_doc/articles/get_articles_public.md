# GET /articles/public

List Public Articles. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | ArticleCategoryEnum | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "slug": "string",
      "title": "string",
      "author": "string",
      "category": "string",
      "cover_image_url": "string",
      "read_time": 0,
      "summary": "",
      "published_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
