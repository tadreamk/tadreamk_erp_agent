# DELETE /payslip-workflow/{workflow_id}

Soft delete a payslip workflow. Can only delete when status is `pending_payment`. Also deletes the linked expense record. Requires `payslip` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Response:**
```json
{
  "message": "Payslip deleted"
}
```

**Errors:**
- `400` — Can only delete during `pending_payment` status
- `401` — Not authenticated
- `403` — Not on payslip whitelist
- `404` — Payslip workflow not found
