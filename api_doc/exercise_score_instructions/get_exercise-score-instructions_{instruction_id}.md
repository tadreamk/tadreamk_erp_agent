# GET /exercise-score-instructions/{instruction_id}

Get exercise score instruction by ID. Requires `exercise` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instruction_id | uuid | Yes | Score instruction ID |

**Response:**
```json
{
  "id": "uuid",
  "title": "Standard Scoring",
  "content": "Score based on...",
  "post_active": true,
  "created_by": "string",
  "updated_by": "string|null",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `400` — Invalid instruction ID format
- `401` — Not authenticated
- `403` — No exercise whitelist access
- `404` — Score instruction not found
