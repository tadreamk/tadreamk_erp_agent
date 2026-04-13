# GET /exercises/active-list

Get list of active exercises for dropdown selection. Requires `exercise` whitelist.

**Response:**
```json
{
  "exercises": [
    {
      "id": "uuid",
      "slug": "exercise-slug",
      "title": "Exercise Title"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
