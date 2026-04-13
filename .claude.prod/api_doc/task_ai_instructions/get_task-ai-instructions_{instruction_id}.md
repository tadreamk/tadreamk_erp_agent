# GET /task-ai-instructions/{instruction_id}

Get task AI instruction by ID. Requires `task` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | AI instruction ID |

**Response:**
```json
{
  "id": "uuid",
  "title": "My AI Instruction",
  "content": "When creating tasks, always...",
  "post_active": true,
  "username": "current_user",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `403` — No task whitelist access
- `404` — AI instruction not found
