# POST /task-ai-instructions


Create a new task AI instruction. The instruction is owned by the authenticated user.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Instruction title (1-255 chars) |
| content | string | Yes | AI feedback instruction content in Markdown (min 1 char) |
| post_active | bool | No | Whether instruction is active (default: true) |

**Response (201):**
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
- `500` — Failed to create AI instruction
