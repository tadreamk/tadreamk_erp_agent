# GET /tasks


Get list of tasks where the current user is a member.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter_by_role | string | No | Filter by role: `manager`, `member`, or omit for both |

**Response:**
```json
{
  "tasks": [
    {
      "id": "uuid",
      "slug": "task-abc123",
      "title": "Implement login page",
      "description": "Build the login form with validation",
      "priority": "high",
      "status": "in_progress",
      "members": [
        { "username": "john.doe", "role": "manager" },
        { "username": "jane.smith", "role": "member" }
      ],
      "active_bot_comment": true,
      "ai_instruction_id": "uuid",
      "start_date": "2025-07-01",
      "end_date": "2025-07-15",
      "project_id": "uuid",
      "project": {
        "id": "uuid",
        "title": "Web Redesign",
        "color_code": "#6366f1"
      },
      "created_at": "2025-06-28T10:00:00+00:00",
      "modified_at": "2025-07-02T14:30:00+00:00",
      "created_by": "john.doe",
      "updated_by": "jane.smith"
    }
  ],
  "total": 1
}
```

**Note:** If the user has no access, returns `{ "tasks": [], "total": 0, "message": "No access" }`.

**Errors:**
- `401` — Not authenticated
