# POST /api/v1/payslip-workflow/batch


Create payslips for multiple employees at once. Also creates a linked expense record for each payslip.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| template_id | UUID | Yes | Payslip template ID |
| payroll_month | string | Yes | Payroll month in `YYYY-MM` format |
| employee_usernames | string[] | Yes | List of employee usernames (min 1) |

**Request example:**
```json
{
  "template_id": "a1b2c3d4-...",
  "payroll_month": "2026-03",
  "employee_usernames": ["john.doe", "jane.smith"]
}
```

**Response:**
```json
{
  "created_count": 2,
  "payslip_ids": ["uuid-1", "uuid-2"],
  "message": "Created 2 payslips"
}
```

If some employees fail (e.g., duplicate month or missing contract):
```json
{
  "created_count": 1,
  "payslip_ids": ["uuid-1"],
  "message": "Created 1 payslips. Errors: Payslip exists for jane.smith in 2026-03"
}
```

**Errors:**
- `400` -- Template not found
- `400` -- Funding allocation error when creating linked expense
- `401` -- Not authenticated
- `403` -- No access to payslip section
