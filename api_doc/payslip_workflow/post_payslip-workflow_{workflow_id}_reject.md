# POST /payslip-workflow/{workflow_id}/reject

Finance rejects a payslip with a reason. Transitions status to `finance_rejected` (terminal). The linked expense reverts to `unallocated`. Requires `payslip` whitelist access (Finance).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Request Body:**
```json
{
  "reason": "string (required) -- rejection reason"
}
```

**Response:**
```json
{
  "message": "Payslip rejected by finance",
  "status": "finance_rejected",
  "reason": "the rejection reason provided"
}
```

**Errors:**
- `400` -- Payslip must be in `pending_payment` or `finance_confirmed` status
- `401` -- Not authenticated
- `403` -- Not on payslip whitelist
- `404` -- Payslip workflow not found
