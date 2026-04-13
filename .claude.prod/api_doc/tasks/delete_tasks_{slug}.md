# DELETE /tasks/{slug}

Delete a task. Cascade deletes all comments and members. Requires manager role on the task. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |

**Response:**
```json
{
  "status": 200,
  "message": "Task deleted successfully",
  "data": { "slug": "task-slug" }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Must be a task manager to delete
- `404` — Task not found
