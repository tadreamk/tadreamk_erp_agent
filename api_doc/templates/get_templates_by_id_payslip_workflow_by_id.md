# GET /templates/{template_id}/payslip-workflow/{workflow_id}


Get template with field values populated from a payslip workflow. Access is granted to the employee who owns the payslip or users with `payslip` whitelist access.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| template_id | string (UUID) | Yes | Template unique identifier |
| workflow_id | string (UUID) | Yes | Payslip workflow unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "title": "Payslip Template",
  "description": "Monthly payslip",
  "category": "payslip",
  "fields": [],
  "pdf_url": null,
  "is_active": true,
  "version": 1,
  "created_at": "2026-01-10T08:00:00+00:00",
  "updated_at": "2026-01-10T08:00:00+00:00",
  "field_values": {
    "basic_salary": "5000",
    "deductions": "500"
  },
  "payslip_workflow_id": "uuid",
  "payroll_month": "2026-03",
  "user_role": "employee",
  "status": "approved"
}
```

**`user_role` values:** `employee`, `hr`

**Errors:**
- `400` — Invalid workflow ID format / Template ID mismatch
- `401` — Not authenticated
- `403` — No access to this payslip
- `404` — Payslip workflow not found
