# POST /equipment/{equipment_id}/transfer


Transfer equipment from one employee to another. Sends a notification and email to the new employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | Equipment record ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_username | string | Yes | New employee username |
| assigned_date | date | No | Transfer date (defaults to today) |

**Response:** Same as `GET /equipment/{equipment_id}`.

**Errors:**
- `400` — Employee username not found
- `401` — Not authenticated
- `403` — No access to equipment management
- `404` — Equipment not found
