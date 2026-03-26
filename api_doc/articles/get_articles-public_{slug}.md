# GET /articles-public/{slug}

Get a single published article by its slug. No authentication required. Returns 404 if the article does not exist or is not published.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly article slug |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "slug": "string",
  "summary": "string",
  "content": "string",
  "category": "string",
  "status": "published",
  "publish_date": "datetime"
}
```

**Errors:**
- `404` — Article not found or not published
