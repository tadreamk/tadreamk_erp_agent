# GET /task-ai-instructions/{instruction_id}


Get a task AI instruction by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | string (UUID) | AI instruction ID |

**Response:**
```json
{
  "id": "uuid",
  "title": "Concise Code Review",
  "content": "Review the code changes and provide concise feedback...",
  "post_active": true,
  "username": "john.doe",
  "created_at": "2025-06-01T08:00:00",
  "updated_at": "2025-06-15T10:00:00"
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `404` — AI instruction not found
