# PUT /exercise-score-instructions/{instruction_id}


Update an existing score instruction. Only provided fields are updated; omitted fields remain unchanged.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | UUID | Score instruction ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Instruction title (1--255 chars) |
| content | string | No | Scoring instruction content in Markdown (min 1 char) |
| post_active | bool | No | Whether the instruction is active |

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
- `400` -- Invalid instruction ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Score instruction not found
- `500` -- Internal server error
