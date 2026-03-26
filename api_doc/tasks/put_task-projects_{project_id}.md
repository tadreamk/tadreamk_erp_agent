# PUT /task-projects/{project_id}

Update an existing task project. Requires `task` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | UUID | The task project's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Updated project title |
| description | string | No | Updated description |
| color_code | string | No | Updated color code |
| post_active | boolean | No | Active status |

**Response:**
```json
{
  "success": true,
  "message": "Task project updated successfully",
  "data": { "id": "uuid" }
}
```

**Errors:**
- `400` — Invalid project ID format
- `401` — Not authenticated
- `403` — No `task` whitelist access
- `404` — Task project not found
