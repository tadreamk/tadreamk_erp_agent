# Librarian API

Base prefix: `/librarian`

Authentication: Required. All endpoints require `librarian` whitelist access.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/librarian/chat` | Send a message and get a permission-filtered response |
| GET | `/librarian/history` | Get librarian conversation history |

## Endpoint Documentation

- [POST /librarian/chat](post_librarian_chat.md)
- [GET /librarian/history](get_librarian_history.md)
