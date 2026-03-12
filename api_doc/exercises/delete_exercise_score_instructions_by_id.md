# DELETE /exercise-score-instructions/{instruction_id}


Soft-delete a score instruction (sets `post_active` to `false`).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | UUID | Score instruction ID |

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
- `400` -- Invalid instruction ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Score instruction not found
