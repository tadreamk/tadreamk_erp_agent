# POST /tasks

Create New Task. Public endpoint (no auth).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Task title |
| description | string | No | Task description |
| priority | string | No | Task priority (low, medium, high, urgent, critical) |
| status | string | No | Task status: not_started, in_queue, in_progress, blocked, request_approval, completed, cancelled |
| members | array[TaskMemberInput] | No | List of task members with roles |
| active_bot_comment | boolean | No | Enable AI-generated comments after member comments |
| start_date | string | No | Task start date (defaults to today) |
| end_date | string | No | Task end date (optional) |
| project_id | string | No | Project ID this task belongs to |
| ai_instruction_id | string | No | AI instruction ID for custom feedback |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
