# GET /payslip-workflow

List all payslip workflows (HR view). Requires `payslip` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| payroll_month | string | No | Filter by payroll month (e.g. "2024-01") |
| employee_username | string | No | Filter by employee username |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 500) |

**Response:**
```json
{
  "payslips": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "employee_name": "John Doe",
      "payroll_month": "2024-01",
      "status": "employee_signature",
      "created_at": "datetime"
    }
  ],
  "total": 15,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on payslip whitelist
