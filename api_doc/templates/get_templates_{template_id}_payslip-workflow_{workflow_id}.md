# GET /templates/{template_id}/payslip-workflow/{workflow_id}

Get a template with field values pre-filled from a payslip workflow. Accessible by the employee themselves or users with `payslip` whitelist access. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | UUID | The template's unique identifier |
| workflow_id | UUID | The payslip workflow's unique identifier |

**Response:** Template object with additional fields
```json
{
  "id": "uuid",
  "name": "string",
  "field_values": {},
  "payslip_workflow_id": "uuid",
  "payroll_month": "2024-01",
  "user_role": "employee",
  "status": "employee_signature"
}
```

**Errors:**
- `400` — Invalid template or workflow ID format; or template ID mismatch
- `401` — Not authenticated
- `403` — No access to this payslip
- `404` — Template or payslip workflow not found
