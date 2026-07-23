# POST /expenses

Create Expense Route. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| expense_category_id | string | Yes |  |
| total_value | number|string | Yes |  |
| note | string | No |  |
| file_urls | array[object] | No |  |

**Response:**
```json
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
      "funding_source_id": "uuid",
      "amount": "string",
      "source_name": "string"
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
```

**Errors:**
- `422` — Validation Error
