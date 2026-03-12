# GET /task-projects/active-list


Get list of active task projects for dropdown selection. Only requires authentication (no whitelist).

**Response:**
```json
{
  "projects": [
    { "id": "uuid", "title": "Web Redesign" },
    { "id": "uuid", "title": "Mobile App" }
  ]
}
```

**Errors:**
- `401` — Not authenticated
