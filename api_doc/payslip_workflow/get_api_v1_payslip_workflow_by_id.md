# GET /api/v1/payslip-workflow/{workflow_id}


Get payslip workflow details. Accessible by HR, CEO, and the employee (employee can only view when status is `employee_signature` or `completed`).

**Access control:** Whitelist `payslip` or `payslip-ceo`, or the payslip's employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "john.doe",
  "employee_name": "Doe, John",
  "employee_email": "john.doe@company.com",
  "hr_username": "hr.admin",
  "payroll_month": "2026-03",
  "status": "pending_payment",
  "field_values": {
    "family_name": "Doe",
    "given_name": "John",
    "monthly_salary": 30000
  },
  "template_id": "template-uuid",
  "template_name": "Standard Payslip",
  "template_fields": [{"name": "monthly_salary", "type": "number"}],
  "signed_at": null,
  "pdf_url": null,
  "created_at": "2026-03-01T10:00:00",
  "updated_at": null,
  "is_active": true,
  "can_edit": true,
  "can_delete": true,
  "can_confirm": true,
  "can_resend": false,
  "can_approve": false,
  "can_reject": false,
  "can_sign": false,
  "is_completed": false,
  "linked_expense_id": "expense-uuid",
  "expense_data": {
    "id": "expense-uuid",
    "funding_allocation": [],
    "total_value": 25000.0,
    "total_allocated": 0,
    "is_fully_allocated": false
  }
}
```

**Role-based action flags:**
| Flag | HR | CEO | Employee |
|------|-----|-----|----------|
| can_edit | `pending_payment`, `finance_confirmed`, `ceo_approval` | -- | -- |
| can_delete | `pending_payment` | -- | -- |
| can_confirm | `pending_payment` | -- | -- |
| can_resend | `finance_confirmed` | -- | -- |
| can_approve | -- | `ceo_approval` | -- |
| can_reject | -- | `ceo_approval` | -- |
| can_sign | -- | -- | `employee_signature` |

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to this payslip
- `404` -- Payslip workflow not found (also returned when employee views a payslip not yet at `employee_signature` or `completed`)
