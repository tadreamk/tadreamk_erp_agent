# GET /expenses


List all expenses with optional filters and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status: `pending`, `finished` |
| expense_category_id | UUID | No | Filter by expense category ID |
| source_type | string | No | Filter by source: `payslip`, `reimbursement`, `manual` |
| skip | int | No | Offset for pagination (default: 0, min: 0) |
| limit | int | No | Items per page (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "expense_category_id": "uuid",
    "expense_category_name": "Salaries & Wages",
    "total_value": 5000.00,
    "status": "pending",
    "source_type": "payslip",
    "is_fully_allocated": false,
    "created_at": "2026-03-01T10:00:00",
    "payroll_employee": "john.doe",
    "reimbursement_employee": null
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to expense management
