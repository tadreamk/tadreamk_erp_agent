# GET /expenses

List all expenses with optional filters. Requires `expense-management` whitelist or CEO role.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| expense_category_id | UUID | No | Filter by category |
| source_type | string | No | Filter by source type (payslip, reimbursement, timesheet, manual) |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "string",
    "amount": 1000.0,
    "currency": "HKD",
    "status": "pending",
    "expense_category_id": "uuid",
    "source_type": "manual",
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
