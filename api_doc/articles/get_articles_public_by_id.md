# GET /articles-public/{slug}


Get a single published article by slug. No authentication required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Article slug |

**Response:** Single article object.

**Errors:**
- `404` — Article not found or not published
