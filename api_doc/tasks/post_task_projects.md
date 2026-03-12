# POST /task-projects/


Create a new task project.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Project title (1-255 chars) |
| description | string | No | Project description (max 2000 chars) |
| color_code | string | No | Hex color code (4-20 chars, default: `#6366f1`) |
| post_active | bool | No | Whether project is active (default: true) |

**Response (201):**
```json
{
  "success": true,
  "message": "Task project created successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — You don't have access to manage task projects
- `500` — Failed to create task project
