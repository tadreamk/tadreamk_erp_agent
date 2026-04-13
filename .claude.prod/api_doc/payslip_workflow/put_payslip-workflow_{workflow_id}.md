# PUT /payslip-workflow/{workflow_id}

Update payslip field values. Only allowed when status is not `completed`. For hourly contracts, salary is auto-computed when `hours_worked` changes. Requires `payslip` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Map of template field keys to values |

**Response:** Updated payslip workflow object

**Errors:**
- `400` — Cannot edit a completed payslip
- `401` — Not authenticated
- `403` — Not on payslip whitelist
- `404` — Payslip workflow not found
