# GET /task-ai-instructions


Get list of the current user's task AI instructions with filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| post_active | bool | No | Filter by active status (`true` or `false`) |
| page | int | No | Page number (default: 1, min: 1) |
| limit | int | No | Items per page (default: 20, min: 1, max: 100) |

**Response:**
```json
{
  "instructions": [
    {
      "id": "uuid",
      "title": "Concise Code Review",
      "content": "Review the code changes and provide concise feedback...",
      "post_active": true,
      "username": "john.doe",
      "created_at": "2025-06-01T08:00:00",
      "updated_at": "2025-06-15T10:00:00"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 3,
    "total_pages": 1,
    "has_next": false,
    "has_prev": false
  }
}
```

**Errors:**
- `401` — Not authenticated
