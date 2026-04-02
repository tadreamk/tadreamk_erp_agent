# POST /tasks/recurrences

Create a new recurrence template and spawn the first task.

**Auth:** Requires `tasks` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Task title (1-500 chars) |
| description | string | No | Task description (max 5000 chars) |
| priority | string | No | `low`, `medium` (default), `high`, `critical` |
| active_bot_comment | bool | No | Enable AI bot comments (default false) |
| project_id | string | No | Project UUID |
| ai_instruction_id | string | No | AI instruction UUID |
| frequency | string | Yes | `daily`, `weekly`, or `monthly` |
| day_of_week | integer | No | 0 (Mon) - 6 (Sun), for weekly recurrence |
| day_of_month | integer | No | 1-31, for monthly recurrence |
| start_date | date | Yes | When to start generating tasks |
| end_date | date | No | When to stop generating tasks |
| members | array | No | Array of `{username, task_role}` objects |

**Response:** `201 Created`
```json
{
  "status": 201,
  "message": "Recurrence created successfully",
  "data": {
    "recurrence": {
      "id": "uuid",
      "title": "Weekly Standup Notes",
      "description": null,
      "priority": "medium",
      "active_bot_comment": false,
      "ai_instruction_id": null,
      "project_id": null,
      "frequency": "weekly",
      "day_of_week": 1,
      "day_of_month": null,
      "start_date": "2024-01-01",
      "end_date": null,
      "last_generated_date": "2024-01-01",
      "is_active": true,
      "members": [],
      "created_by": "admin",
      "updated_by": "admin",
      "created_at": "2024-01-01T00:00:00",
      "modified_at": "2024-01-01T00:00:00"
    },
    "first_task": { "...task object..." }
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access
