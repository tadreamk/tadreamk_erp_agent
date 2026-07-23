# POST /reimbursement/me/requests

Create My Request. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| reason | string | Yes |  |
| estimated_amount | number|string | Yes |  |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "employee_preferred_name": "string",
  "manager_username": "string",
  "manager_preferred_name": "string",
  "approver_username": "string",
  "approver_preferred_name": "string",
  "ceo_username": "string",
  "ceo_preferred_name": "string",
  "title": "string",
  "reason": "string",
  "estimated_amount": "string",
  "total_value": "string",
  "expense_category_id": "uuid",
  "expense_category_title": "string",
  "linked_expense_id": "uuid",
  "status": "string",
  "file_urls": [
    {}
  ],
  "funding_allocation": [
    {}
  ],
  "funding_allocation_resolved": [
    {
      "funding_source_id": "uuid",
      "amount": "string",
      "source_name": "string"
    }
  ],
  "employee_note": "string",
  "is_active": false,
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
