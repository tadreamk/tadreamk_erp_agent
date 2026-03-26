# DELETE /articles/{article_id}

Delete an article permanently.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| article_id | UUID | The article's unique identifier |

**Response:**
```json
{
  "message": "Article deleted"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
- `404` — Article not found
