# POST /reimbursement-workflow

Create a new reimbursement pre-approval request. Status defaults to `pending_pre_approval`. Notifies the employee's direct manager. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_value | number | Yes | Estimated reimbursement amount |
| file_urls | list[string] | No | URLs of supporting documents (defaults to `[]`, not needed for pre-approval) |
| employee_note | string | No | Description of planned purchase |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "employee_username": "string",
  "total_value": 500.00,
  "status": "pending_pre_approval",
  "file_urls": [],
  "employee_note": "string",
  "created_at": "2024-01-01T00:00:00"
}
```

**Errors:**
- `401` -- Not authenticated
