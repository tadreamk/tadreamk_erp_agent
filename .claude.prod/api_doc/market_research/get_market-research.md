# GET /market-research

List Companies. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | string | No |  |
| tier | integer | No |  |
| country | string | No |  |
| company_size | string | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "name": "string",
      "industry": "string",
      "location_city": "string",
      "location_country": "string",
      "company_size": "string",
      "potential_score": 0,
      "potential_tier": 0,
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
