# PUT /exercises/{exercise_id}/status

Update an exercise's `post_active` status. Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | The exercise's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| post_active | bool | Yes | Whether the exercise is active |

**Response:**
```json
{
  "success": true,
  "message": "Exercise status updated successfully",
  "data": {
    "id": "uuid",
    "post_active": true
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Exercise not found
