# POST /payslips/{payslip_id}/sign

Sign Payslip. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| payslip_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| signature_base64 | string | Yes |  |
| rendered_html | string | No |  |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "employee_preferred_name": "string",
  "template_id": "uuid",
  "payroll_month": "string",
  "status": "string",
  "field_values": {},
  "linked_expense_id": "uuid",
  "signature_base64": "string",
  "signed_at": "datetime",
  "onedrive_url_employee": "string",
  "onedrive_url_admin": "string",
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
