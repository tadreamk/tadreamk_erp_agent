# GET /reimbursement-workflow (Finance)

List all reimbursement workflows (Finance/HR view). Requires `reimbursement-workflow` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| employee_username | string | No | Filter by employee username |
| date_from | datetime | No | Filter by submission date from |
| date_to | datetime | No | Filter by submission date to |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "reimbursements": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "employee_name": "John Doe",
      "total_value": 500.00,
      "status": "submitted",
      "expense_category_title": "Office Supplies",
      "created_at": "datetime"
    }
  ],
  "total": 8,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
