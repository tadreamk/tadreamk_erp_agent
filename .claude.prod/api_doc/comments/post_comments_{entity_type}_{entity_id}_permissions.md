# POST /comments/{entity_type}/{entity_id}/permissions

Grant comment permission to a user for an entity. If an inactive permission already exists, it will be reactivated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string | Type of entity |
| entity_id | UUID | The entity's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to grant permission to |

**Response:** Permission object with `message` field (HTTP 201).

**Errors:**
- `401` — Not authenticated
- `403` — Not admin/moderator
