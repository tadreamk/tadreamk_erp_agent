# POST /articles


Create a new article.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Article title (1-500 chars) |
| category | string | Yes | Category (1-50 chars) |
| author | string | Yes | Author name (1-255 chars) |
| summary | string | No | Brief summary |
| content | string | No | Markdown content |
| cover_image_url | string | No | Cover image URL |
| read_time | int | No | Estimated read time in minutes (default: 5) |
| status | string | No | Initial status (default: `draft`) |

**Response:** Created article object.
