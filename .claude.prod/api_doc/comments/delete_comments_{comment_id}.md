# DELETE /comments/{comment_id}

Soft delete a comment. Only the comment author can delete it. Returns HTTP 204 on success.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| comment_id | UUID | The comment's unique identifier |

**Response:** HTTP 204 No Content.

**Errors:**
- `400` — Invalid comment_id
- `401` — Not authenticated
- `403` — Not the comment author
- `404` — Comment not found
