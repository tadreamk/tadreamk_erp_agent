# GET /articles

List articles with optional filters and pagination. Returns articles along with stats.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category |
| status | string | No | Filter by status (e.g., `draft`, `published`) |
| search | string | No | Full-text search |
| page | int | No | Page number (default: 1, min: 1) |
| limit | int | No | Items per page (default: 20, min: 1, max: 100) |

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
      "status": "draft|published",
      "author": "string",
      "cover_image_url": "string|null",
      "read_time": 5,
      "translations": {},
      "created_by": "string",
      "updated_by": "string|null",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  },
  "stats": {}
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles (not whitelisted)
