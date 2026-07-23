# Librarian API

Base prefixes:
- `/librarian`
- `/librarian/conversations/{conversation_id}`
- `/librarian/ws`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| POST | /librarian/cancel-action | Authenticated | Cancel Action | [post_librarian_cancel-action.md](post_librarian_cancel-action.md) |
| POST | /librarian/chat | Authenticated | Chat | [post_librarian_chat.md](post_librarian_chat.md) |
| POST | /librarian/confirm-action | Authenticated | Confirm Action | [post_librarian_confirm-action.md](post_librarian_confirm-action.md) |
| GET | /librarian/conversations | Authenticated | List Conversations | [get_librarian_conversations.md](get_librarian_conversations.md) |
| GET | /librarian/conversations/{conversation_id}/messages | Authenticated | List Messages | [get_librarian_conversations_{conversation_id}_messages.md](get_librarian_conversations_{conversation_id}_messages.md) |
| WEBSOCKET | /librarian/ws/{conversation_id} | Authenticated | WebSocket /librarian/ws/{conversation_id} | [websocket_librarian_ws_{conversation_id}.md](websocket_librarian_ws_{conversation_id}.md) |
