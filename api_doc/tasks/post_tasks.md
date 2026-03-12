# POST /tasks/


Create a new task. The creator is automatically added as a manager. Notifications and emails are sent to all other members.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Task title (1-500 chars) |
| description | string | No | Task description (max 5000 chars) |
| priority | string | No | Priority: `low`, `medium`, `high`, `urgent`, `critical` (default: `medium`) |
| status | string | No | Status: `not_started`, `in_queue`, `in_progress`, `blocked`, `request_approval`, `completed`, `cancelled` (default: `not_started`) |
| members | array | No | List of members with `username` (string) and `role` (`member` or `manager`) |
| active_bot_comment | bool | No | Enable AI-generated comments after member comments (default: false) |
| start_date | date | Yes | Task start date for timeline view (YYYY-MM-DD) |
| end_date | date | No | Task end date (must not be before start_date) |
| project_id | string | No | Project ID this task belongs to |
| ai_instruction_id | string | No | AI instruction ID for custom feedback |

**Response (201):**
```json
{
  "status": 201,
  "message": "Task created successfully",
  "data": {
    "id": "uuid",
    "slug": "task-abc123",
    "title": "Implement login page",
    "description": "...",
    "priority": "medium",
    "status": "not_started",
    "members": [
      { "username": "john.doe", "role": "manager" }
    ],
    "active_bot_comment": false,
    "ai_instruction_id": null,
    "start_date": "2025-07-01",
    "end_date": null,
    "project_id": null,
    "project": null,
    "created_at": "2025-07-01T08:00:00+00:00",
    "modified_at": "2025-07-01T08:00:00+00:00",
    "created_by": "john.doe",
    "updated_by": "john.doe"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access
- `422` — Validation error (e.g., end_date before start_date)
