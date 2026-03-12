# POST /api/v1/payslip-workflow/{workflow_id}/approve


CEO approves a payslip, advancing it to employee signature. Also marks the linked expense as finished. Transitions status to `employee_signature`. Sends notification and email to the employee.

**Access control:** Whitelist `payslip-ceo` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Response:**
```json
{
  "message": "Payslip approved",
  "status": "employee_signature"
}
```

**Errors:**
- `400` -- Payslip must be in `ceo_approval` status to approve
- `401` -- Not authenticated
- `403` -- No access to payslip CEO approval
- `404` -- Payslip workflow not found
