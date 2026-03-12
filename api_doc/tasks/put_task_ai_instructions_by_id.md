# PUT /task-ai-instructions/{instruction_id}


Update an existing task AI instruction. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | string (UUID) | AI instruction ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Instruction title (1-255 chars) |
| content | string | No | AI feedback instruction content (min 1 char) |
| post_active | bool | No | Whether instruction is active |

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
- `404` — AI instruction not found
- `500` — Failed to update AI instruction
