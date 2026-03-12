# POST /equipment/{equipment_id}/unassign


Unassign equipment from its current employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | Equipment record ID |

**Response:** Same as `GET /equipment/{equipment_id}`.

**Errors:**
- `401` — Not authenticated
- `403` — No access to equipment management
- `404` — Equipment not found
