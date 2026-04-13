# PUT /notifications/{notification_id}/unread

Mark a specific notification as unread (reminder feature). Only the notification recipient can mark it as unread. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| notification_id | UUID | The notification's unique identifier |

**Response:** Updated notification object

**Errors:**
- `400` — Invalid notification_id format
- `401` — Not authenticated
- `404` — Notification not found or not accessible by user
