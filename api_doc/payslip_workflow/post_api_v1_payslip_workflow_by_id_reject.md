# POST /api/v1/payslip-workflow/{workflow_id}/reject


CEO rejects a payslip, sending it back to finance for revision. A rejection comment is automatically created. Transitions status back to `finance_confirmed`. Sends notification and email to HR.

**Access control:** Whitelist `payslip-ceo` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | Yes | Reason for rejection (min 1 character) |

**Request example:**
```json
{
  "reason": "Overtime hours do not match timesheet records"
}
```

**Response:**
```json
{
  "message": "Payslip rejected and sent back to finance",
  "status": "finance_confirmed"
}
```

**Errors:**
- `400` -- Payslip must be in `ceo_approval` status to reject
- `401` -- Not authenticated
- `403` -- No access to payslip CEO approval
- `404` -- Payslip workflow not found
