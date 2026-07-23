# GET /task-projects/active

List Active Task Projects. Requires authentication.

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "color": "string"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
