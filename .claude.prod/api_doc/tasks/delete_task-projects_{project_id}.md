# DELETE /task-projects/{project_id}

Soft delete a task project by setting `post_active` to `false`. Requires `task` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | UUID | The task project's unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Task project deleted successfully",
  "data": { "id": "uuid" }
}
```

**Errors:**
- `400` — Invalid project ID format
- `401` — Not authenticated
- `403` — No `task` whitelist access
- `404` — Task project not found
