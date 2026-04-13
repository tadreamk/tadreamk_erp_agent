# Comments API

CRUD operations for comments on various entity types (tasks, job applications, etc.) and admin permission management.

**Access control:** All comment endpoints require authentication. Updating/deleting comments is restricted to the comment author. Admin endpoints require admin or moderator role.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/comments/mention-stats` | Get mention frequency counts | [get_comments_mention-stats.md](./get_comments_mention-stats.md) |
| `GET` | `/comments/{entity_type}/{entity_id}` | List comments for an entity | [get_comments_{entity_type}_{entity_id}.md](./get_comments_{entity_type}_{entity_id}.md) |
| `POST` | `/comments/{entity_type}/{entity_id}` | Create a comment on an entity | [post_comments_{entity_type}_{entity_id}.md](./post_comments_{entity_type}_{entity_id}.md) |
| `PUT` | `/comments/{comment_id}` | Update a comment (author only) | [put_comments_{comment_id}.md](./put_comments_{comment_id}.md) |
| `DELETE` | `/comments/{comment_id}` | Soft delete a comment (author only) | [delete_comments_{comment_id}.md](./delete_comments_{comment_id}.md) |
| `GET` | `/comments/{entity_type}/{entity_id}/permissions` | List permissions for an entity (admin) | [get_comments_{entity_type}_{entity_id}_permissions.md](./get_comments_{entity_type}_{entity_id}_permissions.md) |
| `POST` | `/comments/{entity_type}/{entity_id}/permissions` | Grant comment permission (admin) | [post_comments_{entity_type}_{entity_id}_permissions.md](./post_comments_{entity_type}_{entity_id}_permissions.md) |
| `DELETE` | `/comments/{entity_type}/{entity_id}/permissions/{username}` | Revoke comment permission (admin) | [delete_comments_{entity_type}_{entity_id}_permissions_{username}.md](./delete_comments_{entity_type}_{entity_id}_permissions_{username}.md) |
