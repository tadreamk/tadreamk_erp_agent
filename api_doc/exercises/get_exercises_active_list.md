# GET /exercises/active-list


Get a lightweight list of active exercises for dropdown/select inputs.

**Response:**
```json
{
  "exercises": [
    { "id": "uuid", "title": "Exercise Title" }
  ]
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
