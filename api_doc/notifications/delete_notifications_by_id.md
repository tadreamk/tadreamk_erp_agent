# DELETE /notifications/{notification_id}


Dismiss (archive) a notification. Dismissed notifications are hidden from the inbox but not permanently deleted. Only the notification recipient can dismiss it.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| notification_id | UUID | Notification unique identifier |

**Response:** `204 No Content`

**Errors:**
- `400` — Invalid notification_id format
- `401` — Not authenticated
- `404` — Notification not found

---

### WebSocket /notifications/ws

Real-time WebSocket endpoint for push notifications. Clients receive notification events as they happen, enabling live updates without polling.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| token | string | Yes | Authentication token |

**Connection flow:**
1. Client connects to `ws://<host>/notifications/ws?token=<auth_token>`
2. Server accepts connection and validates the token
3. On success, server registers the connection and sends a welcome message
4. Server pushes notification events as JSON messages
5. Client keeps the connection alive (server discards any client-sent messages)

**Server-pushed message types:**

Notification event:
```json
{
  "type": "notification",
  "data": { "...notification payload..." }
}
```

Unread count update (cross-tab sync):
```json
{
  "type": "unread_count_update",
  "data": { "count": 5 }
}
```

Comment update signal:
```json
{
  "type": "comment_update",
  "data": { "entity_type": "task", "entity_id": "uuid-string" }
}
```

**Close codes:**
- `4001` — Token required or invalid token

---

## 55. Email Notification Settings

Admin endpoints for managing email notification category toggles. Controls which categories of email notifications are sent system-wide.

**Access control:** Requires `notification-settings` whitelist access for all endpoints.
