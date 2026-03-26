# POST /reimbursement-workflow/{workflow_id}/send-to-ceo

Send an approved reimbursement to CEO for final approval. Requires expense category to be set and funding to be fully allocated. Transitions expense from `unallocated` to `pending`. Requires `reimbursement-workflow` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:**
```json
{
  "message": "Reimbursement sent to CEO for approval",
  "status": "approved"
}
```

**Errors:**
- `400` — Reimbursement not in `approved` status; already sent; category not set; or not fully allocated
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
- `404` — Reimbursement or linked expense not found
