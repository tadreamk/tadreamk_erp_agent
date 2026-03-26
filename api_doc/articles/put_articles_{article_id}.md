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
| status | string | No | Updated status |

**Response:** Updated article object (same shape as POST response).

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
- `404` — Article not found
