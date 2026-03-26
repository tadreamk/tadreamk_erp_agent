# DELETE /exercises/{exercise_id}

Soft delete an exercise (sets `post_active` to false). Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | The exercise's unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Exercise deleted successfully",
  "data": { "id": "uuid" }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Exercise not found
