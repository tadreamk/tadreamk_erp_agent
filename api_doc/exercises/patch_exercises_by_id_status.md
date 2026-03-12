# PATCH /exercises/{exercise_id}/status


Toggle the active/inactive status of an exercise.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | Exercise ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| post_active | bool | Yes | Active status to set |

**Response:**
```json
{
  "success": true,
  "message": "Exercise status updated successfully",
  "data": {
    "id": "uuid",
    "post_active": false
  }
}
```

**Errors:**
- `400` -- Invalid exercise ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Exercise not found
