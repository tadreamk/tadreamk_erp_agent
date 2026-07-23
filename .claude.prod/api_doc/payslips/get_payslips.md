# GET /payslips

List Payslips. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| payroll_month | string | No |  |
| employee_username | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "employee_username": "string",
      "employee_preferred_name": "string",
      "payroll_month": "string",
      "status": "string",
      "net_pay": "0.00",
      "created_by_username": "string",
      "created_by_preferred_name": "string",
      "created_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
