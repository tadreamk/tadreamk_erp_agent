# GET /reimbursement/team/requests

List Team Requests. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
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
          "funding_source_id": {},
          "amount": {},
          "source_name": {}
        }
      ],
      "employee_note": "string",
      "is_active": false,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
