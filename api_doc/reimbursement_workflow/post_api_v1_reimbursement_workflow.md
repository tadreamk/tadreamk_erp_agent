# POST /api/v1/reimbursement-workflow


Create a new reimbursement request. The employee username and approval username are set automatically from the authenticated user and system configuration.

**Access control:** Authentication required (any user).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_value | decimal | Yes | Total reimbursement amount in HKD |
| employee_note | string | No | Additional notes or description |
| file_urls | string[] | No | List of URLs to supporting documents (default: []) |

**Request example:**
```json
{
  "total_value": 1500.00,
  "employee_note": "Client dinner at Restaurant XYZ on 2026-02-28",
  "file_urls": [
    "https://onedrive.example.com/receipt1.pdf",
    "https://onedrive.example.com/receipt2.jpg"
  ]
}
```

**Response (201):**
```json
{
  "id": "uuid",
  "employee_username": "john.doe",
  "approval_username": "finance.head",
  "expense_category": null,
  "status": "submitted",
  "total_value": 1500.00,
  "file_urls": [
    "https://onedrive.example.com/receipt1.pdf",
    "https://onedrive.example.com/receipt2.jpg"
  ],
  "employee_note": "Client dinner at Restaurant XYZ on 2026-02-28",
  "created_at": "2026-03-01T10:00:00",
  "updated_at": null,
  "is_active": true,
  "employee_name": "John Doe",
  "approval_name": "Finance Head",
  "expense_category_title": null,
  "can_edit": true,
  "can_delete": true,
  "can_approve": false,
  "can_reject": false,
  "can_confirm": false
}
```

**Errors:**
- `401` -- Not authenticated
