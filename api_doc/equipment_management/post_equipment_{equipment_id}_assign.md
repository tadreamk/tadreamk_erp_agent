# POST /equipment/{equipment_id}/assign

Assign equipment to an employee. Sends a notification to the employee. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_username | string | Yes | Username of the employee to assign to |
| assigned_date | date | No | Assignment date (defaults to today) |

**Response:** Updated equipment object

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `400` — Employee not found
- `404` — Equipment not found
