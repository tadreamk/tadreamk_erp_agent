# GET /payslip-workflow/{workflow_id}

Get payslip workflow details. Accessible by HR, CEO, or the employee themselves. Employees can only view payslips in `employee_signature` or `completed` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Response:** Payslip workflow object with template and field values

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view this payslip
- `404` — Payslip workflow not found (or employee cannot view at current status)
