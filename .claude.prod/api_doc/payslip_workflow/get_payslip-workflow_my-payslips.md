# GET /payslip-workflow/my-payslips

Get payslips for the authenticated employee. Returns payslips in `employee_signature` or `completed` status only. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "payslips": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "payroll_month": "2024-01",
      "status": "employee_signature",
      "signed_at": "datetime",
      "created_at": "datetime"
    }
  ],
  "total": 3,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
