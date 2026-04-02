# POST /exercises/

Create a new exercise. Requires `exercise` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Exercise title |
| tags | list[string] | No | Tags from predefined list |
| content | string | No | Exercise content (Markdown/HTML) |
| post_active | bool | No | Whether visible to applicants (default: true) |
| score_instruction_id | string | No | ID of scoring instructions |

**Response:**
```json
{
  "success": true,
  "message": "Exercise created successfully",
  "data": {
    "id": "uuid",
    "slug": "exercise-slug"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `409` — Slug already exists
