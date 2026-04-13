# POST /equipment/{equipment_id}/unassign

Unassign equipment from its current employee. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Response:** Updated equipment object

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `404` — Equipment not found
