# GET /task-ai-instructions/active-list


Get list of active AI instructions belonging to the current user, for dropdown selection.

**Response:**
```json
{
  "instructions": [
    { "id": "uuid", "title": "Concise Code Review" },
    { "id": "uuid", "title": "Detailed Analysis" }
  ]
}
```

**Errors:**
- `401` — Not authenticated
