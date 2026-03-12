# POST /exercise-score-instructions/


Create a new score instruction.

**Request Body:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| title | string | Yes | -- | Instruction title (1--255 chars) |
| content | string | Yes | -- | Scoring instruction content in Markdown (min 1 char) |
| post_active | bool | No | `true` | Whether the instruction is active |

**Response (201):**
```json
{
  "success": true,
  "message": "Score instruction created successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `500` -- Internal server error
