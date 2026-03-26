# POST /payslip-workflow/{workflow_id}/confirm

Confirm payslip and send it to CEO for approval. Transitions status to `ceo_approval`. On first confirm (`pending_payment`), requires funding to be fully allocated. Requires `payslip` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Response:**
```json
{
  "message": "Payslip sent to CEO for approval",
  "status": "ceo_approval"
}
```

**Errors:**
- `400` — Payslip must be in `pending_payment` or `finance_confirmed` status; or funding not fully allocated
- `401` — Not authenticated
- `403` — Not on payslip whitelist
- `404` — Payslip workflow not found
