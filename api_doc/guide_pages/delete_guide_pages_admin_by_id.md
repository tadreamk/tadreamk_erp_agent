# DELETE /guide-pages/admin/{page_id}

Delete a guide page.

**Access:** Whitelist `guide-pages` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page_id | UUID | Guide page ID |

**Response:**
```json
{
  "message": "Guide page deleted"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Guide page not found |
