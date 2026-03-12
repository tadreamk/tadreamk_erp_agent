# DELETE /comments/{entity_type}/{entity_id}/permissions/{username}


Revoke comment permission from a user for an entity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Entity type identifier |
| entity_id | UUID | Entity unique identifier |
| username | string | Username to revoke permission from |

**Response:** `204 No Content`

**Errors:**
- `400` — Invalid entity_id format / Permission is already revoked
- `401` — Not authenticated
- `403` — Admin or moderator access required
- `404` — Permission not found
