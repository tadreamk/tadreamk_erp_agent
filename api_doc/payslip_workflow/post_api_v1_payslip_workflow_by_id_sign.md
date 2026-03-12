# POST /api/v1/payslip-workflow/{workflow_id}/sign


Employee signs/acknowledges a payslip. Only allowed when status is `employee_signature` and only by the payslip's employee. Transitions status to `completed`. Sends notification and email to HR.

**Access control:** Must be the payslip's employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| signature_data | string | Yes | Base64-encoded signature image |

**Request example:**
```json
{
  "signature_data": "data:image/png;base64,iVBORw0KGgo..."
}
```

**Response:**
```json
{
  "message": "Payslip signed successfully",
  "status": "completed"
}
```

**Errors:**
- `400` -- Cannot sign. Current status: {status}
- `401` -- Not authenticated
- `403` -- Only the employee can sign their payslip
- `404` -- Payslip workflow not found

---

## 38. Payslip Workflow (Approval)
