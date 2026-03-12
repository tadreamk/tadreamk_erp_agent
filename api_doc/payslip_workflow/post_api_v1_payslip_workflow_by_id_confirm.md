# POST /api/v1/payslip-workflow/{workflow_id}/confirm


Finance confirms a payslip and sends it to the CEO for approval. Allowed from `pending_payment` (requires full funding allocation) or `finance_confirmed` (re-send after rejection). Transitions status to `ceo_approval`.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Response:**
```json
{
  "message": "Payslip sent to CEO for approval",
  "status": "ceo_approval"
}
```

**Errors:**
- `400` -- Payslip must be in `pending_payment` or `finance_confirmed` status
- `400` -- Funding must be fully allocated before confirming (only when confirming from `pending_payment`)
- `401` -- Not authenticated
- `403` -- No access to payslip section
- `404` -- Payslip workflow not found
