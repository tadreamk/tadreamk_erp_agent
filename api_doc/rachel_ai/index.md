# Rachel AI API

Base prefix: `/rachel-ai`

Authentication: Required. All endpoints require `rachel-ai` whitelist access.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/rachel-ai/chat` | Send a message to Rachel AI and get a response |
| GET | `/rachel-ai/history` | Get conversation history for the current user |

## Endpoint Documentation

- [POST /rachel-ai/chat](post_rachel-ai_chat.md)
- [GET /rachel-ai/history](get_rachel-ai_history.md)
