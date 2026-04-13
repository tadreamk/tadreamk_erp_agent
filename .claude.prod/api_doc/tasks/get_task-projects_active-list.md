# GET /task-projects/active-list

Get a list of active task projects for dropdown selection. Requires authentication (no whitelist needed).

**Response:**
```json
{
  "projects": [
    { "id": "uuid", "title": "Project Alpha" }
  ]
}
```

**Errors:**
- `401` — Not authenticated
