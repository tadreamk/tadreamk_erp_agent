# POST /comments/{entity_type}/{entity_id}

Create a new comment on an entity. Triggers notifications and AI feedback (for tasks if enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Type of entity (e.g., `task`) |
| entity_id | UUID | The entity's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Comment text |
| image_url | string | No | URL of an attached image |
| audio_url | string | No | URL of an attached audio file |
| mentioned_users | list[string] | No | Usernames mentioned in the comment |

**Response:** Created comment object (HTTP 201).

**Errors:**
- `400` — Invalid entity_id
- `401` — Not authenticated
- `403` — No permission to comment on this entity
