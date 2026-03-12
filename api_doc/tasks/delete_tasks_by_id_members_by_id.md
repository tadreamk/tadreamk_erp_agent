# DELETE /tasks/{slug}/members/{username}


Remove a member from a task. Managers only. Cannot remove the last manager.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Task slug |
| username | string | Username of member to remove |

**Response:**
```json
{
  "status": 200,
  "message": "Member removed successfully",
  "data": {
    "username": "jane.smith"
  }
}
```

**Errors:**
- `400` — Cannot remove the last manager from the task
- `401` — Not authenticated
- `403` — No access to this task / Only managers can perform this action
- `404` — Task not found / Member not found
