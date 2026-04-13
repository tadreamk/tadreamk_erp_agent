# PUT /exercise-score-instructions/{instruction_id}

Update an existing exercise score instruction. Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | Score instruction ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Instruction title |
| content | string | No | Scoring instruction content |
| post_active | bool | No | Whether active |

**Response:**
```json
{
  "success": true,
  "message": "Score instruction updated successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Score instruction not found
- `500` — Failed to update score instruction
