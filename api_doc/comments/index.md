# Comments API

Comment system for entities (tasks, applications, leave requests, payslip workflows, reimbursement workflows, expense management, technical reports). Supports text, image, and audio attachments with @mention notifications.

**Authentication:** All endpoints require authentication. Entity-specific permission checks apply (e.g., task members, application owners, whitelist users).

**Supported entity types:** `task`, `application`, `leave_request`, `payslip_workflow`, `reimbursement_workflow`, `expense_management`, `technical_report`

---

## 52. Comments

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/comments/mention-stats` | Get global mention frequency counts for ranking @mention suggestions in the UI.  | [get_comments_mention_stats.md](./get_comments_mention_stats.md) |
| `GET` | `/comments/{entity_type}/{entity_id}` | List all comments for an entity. | [get_comments_by_id_by_id.md](./get_comments_by_id_by_id.md) |
| `POST` | `/comments/{entity_type}/{entity_id}` | Create a new comment on an entity. Triggers in-app notifications and email notif | [post_comments_by_id_by_id.md](./post_comments_by_id_by_id.md) |
| `PUT` | `/comments/{comment_id}` | Update a comment. Only the comment author can update their own comments. | [put_comments_by_id.md](./put_comments_by_id.md) |
| `DELETE` | `/comments/{comment_id}` | Soft delete a comment. Only the comment author can delete their own comments. Th | [delete_comments_by_id.md](./delete_comments_by_id.md) |
| `GET` | `/comments/{entity_type}/{entity_id}/permissions` | List all active comment permissions for an entity. | [get_comments_by_id_by_id_permissions.md](./get_comments_by_id_by_id_permissions.md) |
| `POST` | `/comments/{entity_type}/{entity_id}/permissions` | Grant comment permission to a user for an entity. If a revoked permission alread | [post_comments_by_id_by_id_permissions.md](./post_comments_by_id_by_id_permissions.md) |
| `DELETE` | `/comments/{entity_type}/{entity_id}/permissions/{username}` | Revoke comment permission from a user for an entity. | [delete_comments_by_id_by_id_permissions_by_id.md](./delete_comments_by_id_by_id_permissions_by_id.md) |
