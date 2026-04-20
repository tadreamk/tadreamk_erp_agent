# GET /expenses

List all expenses with optional filters. Requires `expense-management` whitelist or CEO role.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| expense_category_id | UUID | No | Filter by category |
| source_type | string | No | Filter by source type (payslip, reimbursement, timesheet, manual) |
| q | string | No | Word-split text search — each word matched with ILIKE across note, category name, and employee username; results ordered by relevance score DESC |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 100) |

**Response:**
```json
{
  "expenses": [
    {
      "id": "uuid",
      "title": "Payslip - john.doe - 2026-04",
      "expense_category_id": "uuid",
      "expense_category_name": "Manpower",
      "total_value": 1000.0,
      "status": "pending",
      "source_type": "payslip",
      "is_fully_allocated": false,
      "created_at": "datetime",
      "payroll_employee": "john.doe",
      "reimbursement_employee": null,
      "timesheet_employee": null
    }
  ],
  "total": 20,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
