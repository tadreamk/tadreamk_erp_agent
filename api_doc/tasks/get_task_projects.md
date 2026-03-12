# GET /task-projects/


Get list of task projects with filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| post_active | bool | No | Filter by active status (`true` or `false`) |
| page | int | No | Page number (default: 1, min: 1) |
| limit | int | No | Items per page (default: 20, min: 1, max: 100) |

**Response:**
```json
{
  "projects": [
    {
      "id": "uuid",
      "title": "Web Redesign",
      "description": "Complete website redesign project",
      "color_code": "#6366f1",
      "post_active": true,
      "created_at": "2025-06-01T08:00:00",
      "updated_at": "2025-06-15T10:00:00",
      "created_by": "admin",
      "updated_by": "admin"
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
- `403` — You don't have access to manage task projects
