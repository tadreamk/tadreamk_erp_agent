# POST /tasks/

Create a new task. The creator is automatically added as a task manager. Sends notifications and emails to all other members. Requires `task` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Task title |
| description | string | No | Task description |
| status | string | No | Task status |
| priority | string | No | Task priority |
| start_date | date | No | Task start date |
| end_date | date | No | Task end date |
| project_id | UUID | No | Associated task project |
| members | list | No | Initial member usernames and roles |

**Response:** `201 Created`
```json
{
  "status": 201,
  "message": "Task created successfully",
  "data": { "...task object with members..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `task` whitelist access
