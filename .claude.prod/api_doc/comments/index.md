# Comments API

Base prefixes:
- `/comments`
- `/comments/{entity_type}`
- `/comments/{entity_type}/{entity_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| DELETE | /comments/{comment_id} | Public | Delete Thread Comment | [delete_comments_{comment_id}.md](delete_comments_{comment_id}.md) |
| PUT | /comments/{comment_id} | Public | Update Thread Comment | [put_comments_{comment_id}.md](put_comments_{comment_id}.md) |
| GET | /comments/{entity_type}/{entity_id} | Authenticated | List Thread | [get_comments_{entity_type}_{entity_id}.md](get_comments_{entity_type}_{entity_id}.md) |
| POST | /comments/{entity_type}/{entity_id} | Authenticated | Create Thread Comment | [post_comments_{entity_type}_{entity_id}.md](post_comments_{entity_type}_{entity_id}.md) |
| POST | /comments/{entity_type}/{entity_id}/attachments | Authenticated | Upload Attachment | [post_comments_{entity_type}_{entity_id}_attachments.md](post_comments_{entity_type}_{entity_id}_attachments.md) |
