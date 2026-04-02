# GET /tasks

List tasks where the authenticated user is a member (manager or member). Returns empty list if user has no `task` whitelist access. Requires authentication.

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
      "slug": "string",
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "start_date": "2024-01-01",
      "end_date": "2024-12-31",
      "active_bot_comment": null,
      "ai_instruction_id": null,
      "project_id": null,
      "project": null,
      "recurrence_id": null,
      "members": [],
      "created_at": "datetime",
      "modified_at": "datetime",
      "created_by": "string",
      "updated_by": "string"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
