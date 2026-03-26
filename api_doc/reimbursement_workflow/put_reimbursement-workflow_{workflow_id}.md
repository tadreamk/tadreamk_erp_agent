# PUT /reimbursement-workflow/{workflow_id}

Update a reimbursement workflow. Only the submitting employee can update, and only when status is `submitted`. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_value | number | No | Updated total amount |
| employee_note | string | No | Updated employee note |
| file_urls | list[string] | No | Updated document URLs |

**Response:** Updated reimbursement workflow object

**Errors:**
- `400` — Cannot modify reimbursement in current status
- `401` — Not authenticated
- `403` — Only the submitting employee can update
- `404` — Reimbursement not found
