# GET /customer

List Customers. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | CustomerIndustryEnum | No |  |
| source | CustomerSourceEnum | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "first_name": "string",
      "last_name": "string",
      "position": "string",
      "company_name": "string",
      "email": "string",
      "phone": "string",
      "industry": "string",
      "source": "string",
      "created_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "updated_at": "datetime",
      "updated_by": "string",
      "updated_by_preferred_name": "string"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
