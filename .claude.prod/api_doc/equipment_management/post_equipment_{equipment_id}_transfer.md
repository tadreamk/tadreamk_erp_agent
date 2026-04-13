# POST /equipment/{equipment_id}/transfer

Transfer equipment to another employee. Sends a notification to the new employee. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_username | string | Yes | Username of the new employee |
| assigned_date | date | No | Transfer date (defaults to today) |

**Response:** Updated equipment object

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `400` — Employee not found
- `404` — Equipment not found
