# GET /exercises/tags

Get list of predefined tags available for exercises. Requires `exercise` whitelist.

**Response:**
```json
{
  "tags": ["JavaScript", "Python", "React", "SQL", "Communication"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
