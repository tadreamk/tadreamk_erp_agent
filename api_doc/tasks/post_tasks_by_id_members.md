# POST /tasks/{slug}/members


Add a member to a task. Any existing team member can add new members.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Task slug |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| task_member_username | string | Yes | Username of member to add (1-100 chars) |
| task_role | string | No | Role: `member` or `manager` (default: `member`) |

**Response (201):**
```json
{
  "status": 201,
  "message": "Member added successfully",
  "data": {
    "id": "uuid",
    "task_id": "uuid",
    "task_member_username": "jane.smith",
    "task_role": "member",
    "added_at": "2025-07-05T10:00:00+00:00",
    "added_by": "john.doe"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task
- `404` — Task not found
- `409` — User is already a task member
