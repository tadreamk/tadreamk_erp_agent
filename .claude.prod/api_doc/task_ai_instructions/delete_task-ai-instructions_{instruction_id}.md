# DELETE /task-ai-instructions/{instruction_id}

Soft delete a task AI instruction (sets `post_active` to false). Requires `task` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | AI instruction ID |

**Response:**
```json
{
  "success": true,
  "message": "AI instruction deleted successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `403` — No task whitelist access
- `404` — AI instruction not found
