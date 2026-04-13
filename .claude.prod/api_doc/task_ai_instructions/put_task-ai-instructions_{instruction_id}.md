# PUT /task-ai-instructions/{instruction_id}

Update an existing task AI instruction. Requires `task` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | AI instruction ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Instruction title |
| content | string | No | AI instruction content |
| post_active | bool | No | Whether active |

**Response:**
```json
{
  "success": true,
  "message": "AI instruction updated successfully",
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
- `500` — Failed to update AI instruction
