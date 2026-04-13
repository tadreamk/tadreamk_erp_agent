# GET /tasks

List tasks where the authenticated user is a member (manager or member). Returns empty list if user has no `task` whitelist access. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter_by_role | string | No | Filter by role: `manager`, `member`, or omit for both |
| status | string | No | Filter by task status: `not_started`, `in_queue`, `in_progress`, `blocked`, `request_approval`, `completed`, `cancelled` |
| modified_after | string | No | ISO date (`2026-03-30`) or datetime — tasks modified on or after this timestamp |
| modified_before | string | No | ISO date (`2026-04-13`) or datetime — tasks modified on or before this timestamp |

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
- `400` — Invalid status value
- `401` — Not authenticated
