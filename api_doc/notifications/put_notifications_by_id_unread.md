# PUT /notifications/{notification_id}/unread


Mark a notification as unread (reminder feature). Only the notification recipient can perform this action. Broadcasts an `unread_count_update` WebSocket event for cross-tab synchronization.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| notification_id | UUID | Notification unique identifier |

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "notification_type": "comment",
  "entity_type": "task",
  "entity_id": "660e8400-e29b-41d4-a716-446655440000",
  "title": "New comment on Task #123",
  "message": "john.doe commented on your task",
  "metadata": {},
  "url": "/tasks/660e8400-e29b-41d4-a716-446655440000",
  "created_by": "john.doe",
  "created_at": "2026-03-10T08:30:00+00:00",
  "is_read": false,
  "read_at": null,
  "is_dismissed": false
}
```

**Errors:**
- `400` — Invalid notification_id format
- `401` — Not authenticated
- `404` — Notification not found
