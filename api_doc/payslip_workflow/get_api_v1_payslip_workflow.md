# GET /api/v1/payslip-workflow


List all payslip workflows (HR view) with optional filtering and pagination.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| payroll_month | string | No | Filter by payroll month (`YYYY-MM`) |
| employee_username | string | No | Filter by employee username |
| limit | int | No | Max results (default: 100, range: 1-500) |
| offset | int | No | Pagination offset (default: 0) |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john.doe",
    "employee_name": "Doe, John",
    "payroll_month": "2026-03",
    "status": "pending_payment",
    "created_at": "2026-03-01T10:00:00",
    "signed_at": null,
    "is_active": true,
    "linked_expense_id": "expense-uuid"
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to payslip section
