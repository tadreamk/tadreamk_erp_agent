# DELETE /exercise-score-instructions/{instruction_id}

Soft delete an exercise score instruction (sets `post_active` to false). Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | Score instruction ID |

**Response:**
```json
{
  "success": true,
  "message": "Score instruction deleted successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Score instruction not found
