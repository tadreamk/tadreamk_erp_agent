# DELETE /articles/{article_id}


Delete an article.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | Article ID |

**Response:**
```json
{ "message": "Article deleted" }
```

**Errors:**
- `404` — Article not found
