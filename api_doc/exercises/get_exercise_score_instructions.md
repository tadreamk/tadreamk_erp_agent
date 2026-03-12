# GET /exercise-score-instructions/


List score instructions with filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| post_active | bool | No | -- | Filter by active status |
| page | int | No | 1 | Page number (min 1) |
| limit | int | No | 20 | Items per page (1--100) |

**Response:**
```json
{
  "instructions": [
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
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 5,
    "total_pages": 1,
    "has_next": false,
    "has_prev": false
  }
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
