# GET /articles/{article_id}


Get a single article by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | Article ID |

**Response:** Single article object (same shape as items in list response).

**Errors:**
- `404` — Article not found
