# GET /expenses

List Expenses. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| expense_category_id | string | No |  |
| source | string | No |  |
| q | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "expense_category_id": "uuid",
      "category_name": "string",
      "total_value": "string",
      "note": "string",
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
      "status": "string",
      "approved_at": "datetime",
      "approved_by": "string",
      "approved_by_preferred_name": "string",
      "is_active": false,
      "created_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "updated_at": "datetime",
      "updated_by": "string",
      "updated_by_preferred_name": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
