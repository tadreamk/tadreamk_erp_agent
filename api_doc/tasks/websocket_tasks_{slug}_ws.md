# WebSocket /tasks/{slug}/ws

Real-time task comments stream. Clients connect to receive push events for comments on a specific task. User must be a task member.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| token | string | Yes | JWT authentication token |

**Connection:**
Connect to `ws://<host>/tasks/{slug}/ws?token=<jwt_token>`

**Close codes:**
- `4001` — Token not provided or invalid
- `4003` — No access to this task

**Notes:**
- Send any text message to keep connection alive; client messages are discarded.
- Server pushes comment events in real-time to all connected task members.
