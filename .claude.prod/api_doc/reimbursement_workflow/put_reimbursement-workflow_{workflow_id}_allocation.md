# PUT /reimbursement-workflow/{workflow_id}/allocation

Update the funding allocation for the linked expense of an approved reimbursement. Reimbursement must be in `approved` status. Requires `reimbursement-workflow` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_allocation | list | Yes | List of funding source allocations |

**Response:**
```json
{
  "message": "Allocation updated"
}
```

**Errors:**
- `400` — Reimbursement not in `approved` status; or allocation update failed
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
- `404` — Reimbursement or linked expense not found
