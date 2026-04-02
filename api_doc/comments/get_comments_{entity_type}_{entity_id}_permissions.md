# GET /comments/{entity_type}/{entity_id}/permissions

List all active comment permissions for an entity. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Type of entity |
| entity_id | UUID | The entity's unique identifier |

**Response:**
```json
{
  "permissions": [
    {
      "id": "uuid",
      "entity_type": "task",
      "entity_id": "uuid",
      "username": "alice",
      "created_by": "admin",
      "is_active": true,
      "created_at": "datetime"
    }
  ],
  "total": 2
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not admin/moderator
