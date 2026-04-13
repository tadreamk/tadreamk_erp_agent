# POST /rachel-ai/chat

Send a message to Rachel AI and get a response. Uses recent conversation history (last 5 exchanges) as context. Saves the conversation. Requires `rachel-ai` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| message | string | Yes | The user's message to Rachel AI |

**Response:**
```json
{
  "response": "Rachel's answer to the query...",
  "conversation_id": "uuid"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to Rachel AI
