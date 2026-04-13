# POST /exercise-score-instructions/

Create a new exercise score instruction. Requires `exercise` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Instruction title |
| content | string | Yes | Scoring instruction content |
| post_active | bool | No | Whether active (default: true) |

**Response:**
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
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `500` — Failed to create score instruction
