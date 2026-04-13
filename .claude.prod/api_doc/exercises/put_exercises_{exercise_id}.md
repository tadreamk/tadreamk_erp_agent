# PUT /exercises/{exercise_id}

Update an existing exercise. Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | The exercise's unique identifier |

**Request Body:** (all fields optional, same as POST)

**Response:**
```json
{
  "success": true,
  "message": "Exercise updated successfully",
  "data": {
    "id": "uuid",
    "slug": "exercise-slug"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Exercise not found
