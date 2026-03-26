# Notifications API

Base prefix: `/notifications`

Authentication: Required for all endpoints. WebSocket requires `token` query parameter.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/notifications` | List notifications for the authenticated user |
| GET | `/notifications/unread-count` | Get unread notification count |
| PUT | `/notifications/read-all` | Mark all notifications as read |
| PUT | `/notifications/{notification_id}/read` | Mark a notification as read |
| PUT | `/notifications/{notification_id}/unread` | Mark a notification as unread |
| DELETE | `/notifications/{notification_id}` | Dismiss a notification |
| WebSocket | `/notifications/ws` | Real-time notification stream |

## Endpoint Documentation

- [GET /notifications](get_notifications.md)
- [GET /notifications/unread-count](get_notifications_unread-count.md)
- [PUT /notifications/read-all](put_notifications_read-all.md)
- [PUT /notifications/{notification_id}/read](put_notifications_{notification_id}_read.md)
- [PUT /notifications/{notification_id}/unread](put_notifications_{notification_id}_unread.md)
- [DELETE /notifications/{notification_id}](delete_notifications_{notification_id}.md)
- [WebSocket /notifications/ws](websocket_notifications_ws.md)
