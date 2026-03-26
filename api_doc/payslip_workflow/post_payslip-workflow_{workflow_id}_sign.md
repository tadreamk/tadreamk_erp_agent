# POST /payslip-workflow/{workflow_id}/sign

Employee signs/acknowledges a payslip. Payslip must be in `employee_signature` status. Sends notification and email on success. Requires authentication (employee only).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| signature_data | string | Yes | Employee's signature data (base64 or URL) |

**Response:**
```json
{
  "message": "Payslip signed successfully",
  "status": "completed"
}
```

**Errors:**
- `400` — Payslip not in `employee_signature` status
- `401` — Not authenticated
- `403` — Only the employee can sign their payslip
- `404` — Payslip workflow not found
