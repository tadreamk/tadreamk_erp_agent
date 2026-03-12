# PUT /articles/{article_id}


Update an existing article. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | Article ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Article title (1-500 chars) |
| category | string | No | Category (1-50 chars) |
| author | string | No | Author name (1-255 chars) |
| summary | string | No | Brief summary |
| content | string | No | Markdown content |
| cover_image_url | string | No | Cover image URL |
| read_time | int | No | Estimated read time in minutes |
| status | string | No | Article status |
| translations | object | No | Translation data keyed by language code |

**Response:** Updated article object.

**Errors:**
- `404` — Article not found
