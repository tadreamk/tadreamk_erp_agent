# POST /task-projects/

Create a new task project. Requires `task` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Project title |
| description | string | No | Project description |
| color_code | string | No | Color code for display (e.g. "#FF5733") |

**Response:** `201 Created`
```json
{
  "success": true,
  "message": "Task project created successfully",
  "data": { "id": "uuid" }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `task` whitelist access
- `500` — Failed to create task project
