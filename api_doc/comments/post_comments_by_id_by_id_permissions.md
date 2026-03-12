# POST /comments/{entity_type}/{entity_id}/permissions


Grant comment permission to a user for an entity. If a revoked permission already exists, it will be reactivated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Entity type identifier |
| entity_id | UUID | Entity unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to grant permission (1-100 chars) |

**Response (201):**
```json
{
  "id": "770e8400-e29b-41d4-a716-446655440000",
  "entity_type": "task",
  "entity_id": "660e8400-e29b-41d4-a716-446655440000",
  "username": "john.doe",
  "is_active": true,
  "created_at": "2026-03-10T10:00:00+00:00",
  "created_by": "admin",
  "message": "Permission granted successfully"
}
```

If the permission already existed or was reactivated, the `message` field will read `"Permission already exists or was reactivated"`.

**Errors:**
- `400` — Invalid entity_id format
- `401` — Not authenticated
- `403` — Admin or moderator access required
