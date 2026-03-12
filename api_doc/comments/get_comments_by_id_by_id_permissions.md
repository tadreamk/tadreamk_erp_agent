# GET /comments/{entity_type}/{entity_id}/permissions


List all active comment permissions for an entity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Entity type identifier |
| entity_id | UUID | Entity unique identifier |

**Response:**
```json
{
  "permissions": [
    {
      "id": "770e8400-e29b-41d4-a716-446655440000",
      "entity_type": "task",
      "entity_id": "660e8400-e29b-41d4-a716-446655440000",
      "username": "john.doe",
      "is_active": true,
      "created_at": "2026-03-01T10:00:00+00:00",
      "created_by": "admin"
    }
  ],
  "total": 1
}
```

**Errors:**
- `400` — Invalid entity_id format
- `401` — Not authenticated
- `403` — Admin or moderator access required
