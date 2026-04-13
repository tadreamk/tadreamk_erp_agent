# POST /tasks/{slug}/members

Add a member to a task. Any existing team member can add new members. Sends a notification and email to the new member. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| task_member_username | string | Yes | Username of the user to add |
| task_role | string | Yes | Role to assign: `manager` or `member` |

**Response:** `201 Created`
```json
{
  "status": 201,
  "message": "Member added successfully",
  "data": { "id": "uuid", "task_id": "uuid", "task_member_username": "alice", "task_role": "member", "added_at": "datetime", "added_by": "string" }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task
- `404` — Task not found
- `409` — User is already a task member
