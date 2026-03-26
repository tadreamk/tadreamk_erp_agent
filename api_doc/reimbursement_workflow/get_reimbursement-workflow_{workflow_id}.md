# GET /reimbursement-workflow/{workflow_id}

Get reimbursement workflow details. Accessible by the submitting employee or Finance/HR staff. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:** Reimbursement workflow object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view this reimbursement
- `404` — Reimbursement not found
