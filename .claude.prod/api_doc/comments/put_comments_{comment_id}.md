# PUT /comments/{comment_id}

Update a comment. Only the comment author can update it.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| comment_id | UUID | The comment's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated comment text |
| image_url | string | No | URL of an attached image |
| audio_url | string | No | URL of an attached audio file |

**Response:** Updated comment object.

**Errors:**
- `400` — Invalid comment_id
- `401` — Not authenticated
- `403` — Not the comment author
- `404` — Comment not found
