# GET /tasks/recurrences

List recurrences managed by the authenticated user.

**Auth:** Requires `tasks` whitelist access.

**Response:** `200 OK`
```json
{
  "recurrences": [
    {
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
      "last_generated_date": "2024-01-08",
      "is_active": true,
      "members": [],
      "created_by": "admin",
      "updated_by": "admin",
      "created_at": "2024-01-01T00:00:00",
      "modified_at": "2024-01-01T00:00:00"
    }
  ],
  "total": 1
}
```

**Errors:**
- `401` — Not authenticated
