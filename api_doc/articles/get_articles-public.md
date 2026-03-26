# GET /articles-public

List published articles. No authentication required. Returns only articles with `status=published`, sorted by publish date descending.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 20, max: 100) |

**Response:**
```json
{
  "articles": [
    {
      "id": "uuid",
      "title": "string",
      "slug": "string",
      "summary": "string",
      "category": "string",
      "status": "published",
      "publish_date": "datetime"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "pages": 3
  }
}
```
