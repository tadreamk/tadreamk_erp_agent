# PUT /exercises/{exercise_id}


Update an existing exercise. Only provided fields are updated; omitted fields remain unchanged.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | Exercise ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Exercise title (1--500 chars) |
| tags | string[] | No | Tags from predefined list |
| content | string | No | Markdown content |
| post_active | bool | No | Whether the exercise is active |
| score_instruction_id | string | No | UUID of a score instruction (set `null` to detach) |

**Response:**
```json
{
  "success": true,
  "message": "Exercise updated successfully",
  "data": {
    "id": "uuid",
    "slug": "exercise-title"
  }
}
```

**Errors:**
- `400` -- Invalid exercise ID format, invalid tags, or invalid score instruction ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Exercise not found
