# POST /comments/{entity_type}/{entity_id}


Create a new comment on an entity. Triggers in-app notifications and email notifications to relevant users. For task comments, may also trigger AI feedback generation if enabled on the task.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Entity type (e.g., `task`, `application`, `leave_request`) |
| entity_id | UUID | Entity unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Comment text content (min 1 char) |
| image_url | string | No | Image attachment URL (max 500 chars) |
| audio_url | string | No | Audio attachment URL (max 500 chars) |
| mentioned_users | string[] | No | Usernames to notify. If null, notifies all relevant users |

**Response (201):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "entity_type": "task",
  "entity_id": "660e8400-e29b-41d4-a716-446655440000",
  "username": "john.doe",
  "content": "Updated the design mockups @jane.smith",
  "image_url": null,
  "audio_url": null,
  "is_deleted": false,
  "created_at": "2026-03-10T09:15:00+00:00",
  "updated_at": "2026-03-10T09:15:00+00:00"
}
```

**Side effects:**
- Broadcasts a `comment_update` WebSocket event to all connected users
- Sends in-app notifications to relevant users (filtered by mentions if provided)
- Sends email notifications to task members (for task comments)
- Triggers AI feedback generation in the background (for task comments with `active_bot_comment` enabled)

**Errors:**
- `400` — Invalid entity_id format
- `401` — Not authenticated
- `403` — No permission to comment on this entity
