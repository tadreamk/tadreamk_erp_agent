# PATCH /articles/{article_id}/status


Change article status only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | Article ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | Yes | New status: `draft`, `published`, `archived` |

**Response:** Updated article object.

**Errors:**
- `404` — Article not found
