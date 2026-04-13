# PUT /articles/{article_id}

Update an existing article. Only provided (non-null) fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | The article's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Updated title |
| summary | string | No | Updated summary |
| content | string | No | Updated content |
| category | string | No | Updated category |
| author | string | No | Updated author name |
| cover_image_url | string | No | Updated cover image URL |
| read_time | int | No | Updated read time in minutes |
| translations | dict | No | Updated translations |
| status | string | No | Updated status |

**Response:** Updated article object (same shape as POST response, includes `author`, `cover_image_url`, `read_time`, `translations`, `updated_by`).

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
- `404` — Article not found
