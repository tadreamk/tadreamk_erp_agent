# GET /task-projects/

List task projects with filtering and pagination. Requires `task` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| post_active | boolean | No | Filter by active status |
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (default: 20, max: 100) |

**Response:**
```json
{
  "projects": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "color_code": "#FF5733",
      "post_active": true,
      "created_at": "2024-01-01T00:00:00"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "total_pages": 3,
    "has_next": true,
    "has_prev": false
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `task` whitelist access
