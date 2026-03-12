# GET /articles


List articles with filters, pagination, and stats.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category. Options: `TadReamk AI`, `TadReamk Design`, `IP Law`, `News`, `TadReamk-AIGC`, `TadReamk-ERP` |
| status | string | No | Filter by status: `draft`, `published`, `archived` |
| search | string | No | Search text |
| page | int | No | Page number (default: 1, min: 1) |
| limit | int | No | Items per page (default: 20, min: 1, max: 100) |

**Response:**
```json
{
  "articles": [
    {
      "id": "uuid",
      "slug": "article-slug",
      "category": "News",
      "title": "Article Title",
      "author": "Author Name",
      "cover_image_url": "https://...",
      "summary": "Brief summary",
      "read_time": 5,
      "content": "Markdown content...",
      "translations": { "zh": { "title": "...", "summary": "...", "content": "..." } },
      "status": "draft",
      "publish_date": "2026-01-15T10:00:00+00:00",
      "created_at": "2026-01-10T08:00:00+00:00",
      "updated_at": "2026-01-12T09:00:00+00:00",
      "created_by": "username",
      "updated_by": "username"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "pages": 3
  },
  "stats": { }
}
```
