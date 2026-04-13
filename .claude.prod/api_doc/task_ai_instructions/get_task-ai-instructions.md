# GET /task-ai-instructions

List task AI instructions for the current user with filtering and pagination. Requires `task` whitelist.

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
      "title": "My AI Instruction",
      "content": "When creating tasks, always...",
      "post_active": true,
      "username": "current_user",
      "created_at": "datetime",
      "updated_at": "datetime"
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
- `403` — No task whitelist access
