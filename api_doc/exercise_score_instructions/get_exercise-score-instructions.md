# GET /exercise-score-instructions/

List all exercise score instructions with filtering and pagination. Requires `exercise` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| post_active | bool | No | Filter by active status |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 20, max: 100) |

**Response:**
```json
{
  "instructions": [
    {
      "id": "uuid",
      "title": "Standard Scoring",
      "content": "Score based on...",
      "post_active": true,
      "created_at": "datetime",
      "updated_at": "datetime"
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
- `401` — Not authenticated
- `403` — No exercise whitelist access
