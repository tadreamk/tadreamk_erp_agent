# PATCH /articles/{article_id}/status

Update only the status of an article.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | The article's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | Yes | New status value (e.g., `draft`, `published`) |

**Response:** Updated article object.

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
- `404` — Article not found
