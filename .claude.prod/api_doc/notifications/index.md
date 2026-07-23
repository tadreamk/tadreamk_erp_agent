# Notifications API

Base prefixes:
- `/notification-settings`
- `/notifications`
- `/notifications/{notification_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /notification-settings/ | `)
    settings = email_settings_crud.get_all_settings(db)
    return {
        ` whitelist | List Settings | [get_notification-settings_.md](get_notification-settings_.md) |
| PUT | /notification-settings/{category_key} | `)
    try:
        setting = email_settings_crud.update_setting(
            db,
            category_key,
            is_enabled=payload.is_enabled,
            updated_by=user.username,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    if setting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist | Update Setting | [put_notification-settings_{category_key}.md](put_notification-settings_{category_key}.md) |
| GET | /notifications/ | Authenticated | List Notifications | [get_notifications_.md](get_notifications_.md) |
| PUT | /notifications/read-all | Authenticated | Mark All As Read | [put_notifications_read-all.md](put_notifications_read-all.md) |
| GET | /notifications/unread-count | Authenticated | Get Unread Count | [get_notifications_unread-count.md](get_notifications_unread-count.md) |
| WEBSOCKET | /notifications/ws | Authenticated | WebSocket /notifications/ws | [websocket_notifications_ws.md](websocket_notifications_ws.md) |
| DELETE | /notifications/{notification_id} | Public | Dismiss Notification | [delete_notifications_{notification_id}.md](delete_notifications_{notification_id}.md) |
| PUT | /notifications/{notification_id}/read | Public | Mark As Read | [put_notifications_{notification_id}_read.md](put_notifications_{notification_id}_read.md) |
| PUT | /notifications/{notification_id}/unread | Public | Mark As Unread | [put_notifications_{notification_id}_unread.md](put_notifications_{notification_id}_unread.md) |
