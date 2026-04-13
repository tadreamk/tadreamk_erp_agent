# DELETE /notifications/{notification_id}

Dismiss/archive a notification. Only the notification recipient can dismiss it. Dismissed notifications are hidden from the inbox but not physically deleted. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| notification_id | UUID | The notification's unique identifier |

**Response:** `204 No Content`

**Errors:**
- `400` — Invalid notification_id format
- `401` — Not authenticated
- `404` — Notification not found or not accessible by user
