# GET /exercise-score-instructions/{instruction_id}


Get a single score instruction by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | UUID | Score instruction ID |

**Response:**
```json
{
  "id": "uuid",
  "title": "Scoring Rubric - Backend",
  "content": "# Scoring criteria...",
  "post_active": true,
  "created_at": "2026-01-10T08:00:00+00:00",
  "updated_at": "2026-01-12T14:20:00+00:00",
  "created_by": "admin.user",
  "updated_by": "admin.user"
}
```

**Errors:**
- `400` -- Invalid instruction ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Score instruction not found
