# GET /task-projects/{project_id}


Get a task project by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | string (UUID) | Task project ID |

**Response:**
```json
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
```

**Errors:**
- `400` — Invalid project ID format
- `401` — Not authenticated
- `403` — You don't have access to manage task projects
- `404` — Task project not found
