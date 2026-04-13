# GET /task-ai-instructions/active-list

Get list of active AI instructions for the current user. Requires `task` whitelist.

**Response:**
```json
{
  "instructions": [
    {
      "id": "uuid",
      "title": "My AI Instruction"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No task whitelist access
