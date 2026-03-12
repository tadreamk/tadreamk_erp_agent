# PUT /notifications/read-all


Mark all notifications as read for the authenticated user. Broadcasts an `unread_count_update` WebSocket event with count `0`.

**Response:**
```json
{
  "marked_count": 15
}
```

**Errors:**
- `401` — Not authenticated
