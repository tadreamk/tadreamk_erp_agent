# GET /notification-settings


List all email notification settings with their current enabled/locked status.

**Response:**
```json
{
  "settings": [
    {
      "category_key": "task_comment",
      "description": "Email when someone comments on your task",
      "is_enabled": true,
      "is_locked": false,
      "updated_by": "admin",
      "updated_at": "2026-03-01T10:00:00+00:00"
    },
    {
      "category_key": "leave_status",
      "description": "Email when leave request status changes",
      "is_enabled": true,
      "is_locked": true,
      "updated_by": null,
      "updated_at": null
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No whitelist access to notification-settings
