# DELETE /tasks/{slug}/members/{username}

Remove a member from a task. Requires manager role on the task. Cannot remove the last manager. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |
| username | string | Username of the member to remove |

**Response:**
```json
{
  "status": 200,
  "message": "Member removed successfully",
  "data": { "username": "alice" }
}
```

**Errors:**
- `400` — Cannot remove the last manager from the task
- `401` — Not authenticated
- `403` — Must be a task manager to remove members
- `404` — Task not found or member not found
