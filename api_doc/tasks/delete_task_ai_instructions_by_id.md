# DELETE /task-ai-instructions/{instruction_id}


Soft delete a task AI instruction by setting `post_active` to `false`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | string (UUID) | AI instruction ID |

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
- `400` — Invalid instruction ID
- `401` — Not authenticated
- `404` — AI instruction not found
