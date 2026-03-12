# DELETE /tasks/{slug}


Delete a task and cascade-delete all comments and members. Managers only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Task slug |

**Response:**
```json
{
  "status": 200,
  "message": "Task deleted successfully",
  "data": {
    "slug": "task-abc123"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task / Only managers can perform this action
- `404` — Task not found

---

---

# 50. Task Projects (Admin)

Manage task projects used to group and categorize tasks. Each project has a title, description, and color code displayed in the UI.

**Base path:** `/task-projects`

**Access control:** Authentication required for `GET /task-projects/active-list`. Whitelist `task` required for all other endpoints.
