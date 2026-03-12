# POST /exercises/


Create a new exercise.

**Request Body:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| title | string | Yes | -- | Exercise title (1--500 chars) |
| tags | string[] | No | `[]` | Tags from predefined list |
| content | string | No | `""` | Markdown content |
| post_active | bool | No | `true` | Whether the exercise is active |
| score_instruction_id | string | No | `null` | UUID of a score instruction to attach |

**Response (201):**
```json
{
  "success": true,
  "message": "Exercise created successfully",
  "data": {
    "id": "uuid",
    "slug": "exercise-title"
  }
}
```

**Errors:**
- `400` -- Invalid tags (not in predefined list) or invalid score instruction ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `409` -- Duplicate exercise (slug conflict)
- `500` -- Internal server error
