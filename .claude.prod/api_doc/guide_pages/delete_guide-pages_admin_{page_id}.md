# DELETE /guide-pages/admin/{page_id}

Delete a guide page. Requires `guide-pages` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page_id | UUID | The guide page's unique identifier |

**Response:**
```json
{
  "message": "Guide page deleted"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No guide-pages whitelist access
- `404` — Guide page not found
