# DELETE /comments/{entity_type}/{entity_id}/permissions/{username}

Revoke comment permission from a user for an entity. Returns HTTP 204 on success.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Type of entity |
| entity_id | UUID | The entity's unique identifier |
| username | string | Username whose permission to revoke |

**Response:** HTTP 204 No Content.

**Errors:**
- `400` — Permission is already revoked
- `401` — Not authenticated
- `403` — Not admin/moderator
- `404` — Permission not found
