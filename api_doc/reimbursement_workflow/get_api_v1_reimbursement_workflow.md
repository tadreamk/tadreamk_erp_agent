# GET /api/v1/reimbursement-workflow


List all reimbursement workflows with optional filtering and pagination (Finance view).

**Access control:** Whitelist `reimbursement-workflow` required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| employee_username | string | No | Filter by employee username |
| date_from | datetime | No | Filter by creation date (from) |
| date_to | datetime | No | Filter by creation date (to) |
| limit | int | No | Max results (default: 50, range: 1-200) |
| offset | int | No | Pagination offset (default: 0) |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john.doe",
    "employee_name": "John Doe",
    "approval_username": "finance.head",
    "status": "submitted",
    "total_value": 1500.00,
    "expense_category_title": null,
    "created_at": "2026-03-01T10:00:00",
    "updated_at": null,
    "is_active": true
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to reimbursement workflow
