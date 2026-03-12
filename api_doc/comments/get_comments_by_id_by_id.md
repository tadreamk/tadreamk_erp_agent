# GET /comments/{entity_type}/{entity_id}


List all comments for an entity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Entity type (e.g., `task`, `application`, `leave_request`) |
| entity_id | UUID | Entity unique identifier |

**Response:**
```json
{
  "comments": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "entity_type": "task",
      "entity_id": "660e8400-e29b-41d4-a716-446655440000",
      "username": "john.doe",
      "content": "Updated the design mockups",
      "image_url": "https://storage.example.com/img.png",
      "audio_url": null,
      "is_deleted": false,
      "created_at": "2026-03-10T08:30:00+00:00",
      "updated_at": "2026-03-10T08:30:00+00:00"
    }
  ],
  "total": 1
}
```

**Errors:**
- `400` — Invalid entity_id format (not a valid UUID)
- `401` — Not authenticated
