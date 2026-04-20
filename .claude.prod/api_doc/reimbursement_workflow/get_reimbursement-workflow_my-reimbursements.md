# GET /reimbursement-workflow/my-reimbursements

Get reimbursement workflows for the authenticated user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "reimbursements": [
    {
      "id": "uuid",
      "total_value": 500.00,
      "status": "submitted",
      "expense_category_title": "Office Supplies",
      "created_at": "datetime"
    }
  ],
  "total": 2,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
