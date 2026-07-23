# GET /funding-sources

List Funding Sources. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | FundingTypeEnum | No |  |
| status | FundingStatusEnum | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "source_name": "string",
      "funding_type": "string",
      "provider": "string",
      "reference_no": "string",
      "description": "string",
      "total_approved": "string",
      "start_date": "date",
      "end_date": "date",
      "status": "string",
      "is_active": false,
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
