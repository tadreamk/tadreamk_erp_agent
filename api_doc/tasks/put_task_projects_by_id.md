# PUT /task-projects/{project_id}


Update an existing task project. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | string (UUID) | Task project ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Project title (1-255 chars) |
| description | string | No | Project description (max 2000 chars) |
| color_code | string | No | Hex color code (4-20 chars) |
| post_active | bool | No | Whether project is active |

**Response:**
```json
{
  "success": true,
  "message": "Task project updated successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` — Invalid project ID format
- `401` — Not authenticated
- `403` — You don't have access to manage task projects
- `404` — Task project not found
- `500` — Failed to update task project
