# GET /user-requirements

List Stories. Requires authentication.

**Response:**
```json
{
  "items": [
    {
      "id": "string",
      "title": "string",
      "status": "string",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "updated_by": "string",
      "updated_by_preferred_name": "string",
      "implemented_by": "string",
      "implemented_by_preferred_name": "string",
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
