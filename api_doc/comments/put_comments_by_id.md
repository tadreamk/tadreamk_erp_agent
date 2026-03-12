# PUT /comments/{comment_id}


Update a comment. Only the comment author can update their own comments.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| comment_id | UUID | Comment unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated comment text (min 1 char) |
| image_url | string | No | Updated image attachment URL (max 500 chars) |
| audio_url | string | No | Updated audio attachment URL (max 500 chars) |

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "entity_type": "task",
  "entity_id": "660e8400-e29b-41d4-a716-446655440000",
  "username": "john.doe",
  "content": "Updated content here",
  "image_url": null,
  "audio_url": null,
  "is_deleted": false,
  "created_at": "2026-03-10T09:15:00+00:00",
  "updated_at": "2026-03-10T09:20:00+00:00"
}
```

**Errors:**
- `400` — Invalid comment_id format
- `401` — Not authenticated
- `403` — You can only modify your own comments
- `404` — Comment not found
