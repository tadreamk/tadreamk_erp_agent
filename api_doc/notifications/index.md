# Notifications API

User notification system with real-time WebSocket push support. Notifications are created by backend services (comments, events, workflows) and delivered to specific recipients. Supports read/unread tracking, dismissal, grouping by entity, and cross-tab synchronization via WebSocket broadcasts.

**Authentication:** All endpoints require authentication. Users can only access their own notifications.

---

## 54. Notifications

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/notifications` | List notifications for the authenticated user. Supports pagination, filtering, a | [get_notifications.md](./get_notifications.md) |
| `GET` | `/notifications/unread-count` | Get the count of unread notifications for the authenticated user. | [get_notifications_unread_count.md](./get_notifications_unread_count.md) |
| `PUT` | `/notifications/{notification_id}/read` | Mark a notification as read. Only the notification recipient can perform this ac | [put_notifications_by_id_read.md](./put_notifications_by_id_read.md) |
| `PUT` | `/notifications/{notification_id}/unread` | Mark a notification as unread (reminder feature). Only the notification recipien | [put_notifications_by_id_unread.md](./put_notifications_by_id_unread.md) |
| `PUT` | `/notifications/read-all` | Mark all notifications as read for the authenticated user. Broadcasts an `unread | [put_notifications_read_all.md](./put_notifications_read_all.md) |
| `DELETE` | `/notifications/{notification_id}` | Dismiss (archive) a notification. Dismissed notifications are hidden from the in | [delete_notifications_by_id.md](./delete_notifications_by_id.md) |
| `GET` | `/notification-settings` | List all email notification settings with their current enabled/locked status. | [get_notification_settings.md](./get_notification_settings.md) |
| `PUT` | `/notification-settings/{category_key}` | Toggle an email notification setting on or off. Locked categories cannot be togg | [put_notification_settings_by_id.md](./put_notification_settings_by_id.md) |
