# GET /task-ai-instructions

List Instructions. Requires authentication.

**Response:**
```json
{
  "items": [
    {
      "id": "string",
      "title": "string",
      "brief_description": "string",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
