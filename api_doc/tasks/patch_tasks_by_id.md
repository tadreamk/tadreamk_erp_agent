# PATCH /tasks/{slug}


Update a task. Requires task membership. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Task slug |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Task title (1-500 chars) |
| description | string | No | Task description (max 5000 chars) |
| priority | string | No | Priority: `low`, `medium`, `high`, `urgent`, `critical` |
| status | string | No | Status: `not_started`, `in_queue`, `in_progress`, `blocked`, `request_approval`, `completed`, `cancelled` |
| active_bot_comment | bool | No | Enable/disable AI-generated comments |
| start_date | date | No | Task start date |
| end_date | date | No | Task end date |
| project_id | string | No | Project ID |
| ai_instruction_id | string | No | AI instruction ID |

**Response:**
```json
{
  "status": 200,
  "message": "Task updated successfully",
  "data": {
    "id": "uuid",
    "slug": "task-abc123",
    "title": "Updated title",
    "description": "...",
    "priority": "high",
    "status": "in_progress",
    "members": [],
    "active_bot_comment": false,
    "ai_instruction_id": null,
    "start_date": "2025-07-01",
    "end_date": "2025-07-20",
    "project_id": null,
    "project": null,
    "created_at": "2025-07-01T08:00:00+00:00",
    "modified_at": "2025-07-05T12:00:00+00:00",
    "created_by": "john.doe",
    "updated_by": "jane.smith"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task
- `404` — Task not found

---

### WebSocket /tasks/{slug}/ws

Real-time WebSocket connection for task comments. The server accepts the connection, validates the token, checks task membership, then holds the connection open for real-time comment updates.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Task slug |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| token | string | Yes | Authentication token |

**Close codes:**
- `4001` — Token required or invalid token
- `4003` — No access to this task

---

---

# 49. Tasks (Admin)

Admin operations for task management: adding/removing members and deleting tasks.

**Base path:** `/tasks`

**Access control:** Task membership required for adding members. Manager role within the task required for removing members and deleting tasks.
