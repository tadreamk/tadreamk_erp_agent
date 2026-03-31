# POST /task-ai-instructions

Create a new task AI instruction. Requires `task` whitelist. The instruction is owned by the current user.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Instruction title |
| content | string | Yes | AI instruction content |
| post_active | bool | No | Whether active (default: false) |

**Response:**
```json
{
  "success": true,
  "message": "AI instruction created successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No task whitelist access
- `500` — Failed to create AI instruction
