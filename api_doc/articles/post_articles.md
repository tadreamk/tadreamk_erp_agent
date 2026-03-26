# POST /articles

Create a new article. The creator's username is recorded automatically.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Article title |
| summary | string | No | Short summary |
| content | string | No | Full article content (HTML/Markdown) |
| category | string | No | Article category |
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
  "created_by": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
