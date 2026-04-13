# WebSocket /notifications/ws

Real-time notification stream. Clients connect to receive push notifications as they are created. Authentication via `token` query parameter is required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| token | string | Yes | JWT authentication token |

**Connection:**
Connect to `ws://<host>/notifications/ws?token=<jwt_token>`

Upon successful connection, the server sends a welcome message. The connection remains open to receive push events.

**Server-sent message types:**
```json
{
  "type": "unread_count_update",
  "data": { "count": 5 }
}
```

**Close codes:**
- `4001` — Token not provided or invalid token

**Notes:**
- Send any text message to keep the connection alive; messages from the client are discarded.
- The server broadcasts `unread_count_update` events when read/unread/read-all actions occur across any tab.
