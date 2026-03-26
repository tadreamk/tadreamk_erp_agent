# PUT /comments/{comment_id}

Update a comment. Only the comment author can update it.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| comment_id | UUID | The comment's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Updated comment text |
| mentioned_users | list[string] | No | Updated mentioned usernames |

**Response:** Updated comment object.

**Errors:**
- `400` — Invalid comment_id
- `401` — Not authenticated
- `403` — Not the comment author
- `404` — Comment not found
