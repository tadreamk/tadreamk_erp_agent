# DELETE /task-projects/{project_id}


Soft delete a task project by setting `post_active` to `false`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | string (UUID) | Task project ID |

**Response:**
```json
{
  "success": true,
  "message": "Task project deleted successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` — Invalid project ID
- `401` — Not authenticated
- `403` — You don't have access to manage task projects
- `404` — Task project not found

---

---

# 51. Task AI Instructions (Admin)

Manage custom AI instruction templates that control how AI-generated comments respond to task discussions. Each instruction is user-scoped — users manage their own instructions.

**Base path:** `/task-ai-instructions`

**Access control:** Authentication required for all endpoints. Access is verified via `check_whitelist_access` (all authenticated users have access, filtered by ownership).
