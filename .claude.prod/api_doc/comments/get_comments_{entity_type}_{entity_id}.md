# GET /comments/{entity_type}/{entity_id}

List all active comments for a specific entity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Type of entity (e.g., `task`, `job_application`) |
| entity_id | UUID | The entity's unique identifier |

**Response:**
```json
{
  "comments": [
    {
      "id": "uuid",
      "entity_type": "task",
      "entity_id": "uuid",
      "content": "string",
      "image_url": "string|null",
      "audio_url": "string|null",
      "username": "alice",
      "is_deleted": false,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 5
}
```

**Errors:**
- `400` — Invalid entity_id format
- `401` — Not authenticated
