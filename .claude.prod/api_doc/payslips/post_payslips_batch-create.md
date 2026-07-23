# POST /payslips/batch-create

Batch Create Payslips. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| template_id | string | Yes |  |
| payroll_month | string | Yes |  |
| employee_usernames | array[string] | Yes |  |

**Response:**
```json
{
  "items": [
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
  ],
  "errors": [
    {
      "employee_username": "string",
      "reason": "string"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
