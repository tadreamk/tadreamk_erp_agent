# PUT /equipment/{equipment_id}

Update an existing equipment record. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Request Body:** (all fields optional, same as POST)

**Response:** Updated equipment object

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `404` — Equipment not found
