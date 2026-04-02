# POST /articles

Create a new article. The creator's username is recorded automatically.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Article title |
| summary | string | No | Short summary |
| content | string | No | Full article content (HTML/Markdown) |
| category | string | No | Article category |
| author | string | Yes | Author name |
| cover_image_url | string | No | Cover image URL |
| read_time | int | No | Estimated read time in minutes (default: 5) |
| status | string | No | `draft` or `published` |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "slug": "string",
  "summary": "string",
  "content": "string",
  "category": "string",
  "status": "draft",
  "author": "string",
  "cover_image_url": "string|null",
  "read_time": 5,
  "translations": {},
  "created_by": "string",
  "updated_by": "string|null",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
