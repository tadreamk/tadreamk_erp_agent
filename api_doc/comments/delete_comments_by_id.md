# DELETE /comments/{comment_id}


Soft delete a comment. Only the comment author can delete their own comments. The comment is marked as deleted but not removed from the database.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| comment_id | UUID | Comment unique identifier |

**Response:** `204 No Content`

**Errors:**
- `400` — Invalid comment_id format
- `401` — Not authenticated
- `403` — You can only modify your own comments
- `404` — Comment not found

---

## 53. Comment Permissions (Admin)

Admin endpoints for managing explicit comment permissions on entities. Requires admin or moderator role.

**Access control:** Admin or moderator authentication required for all endpoints.
