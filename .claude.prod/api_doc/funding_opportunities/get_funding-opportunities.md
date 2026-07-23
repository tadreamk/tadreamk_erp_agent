# GET /funding-opportunities

List Funding Opportunities. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| stage | FundingOpportunityStageEnum | No |  |
| funding_type | FundingTypeEnum | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "opportunity_name": "string",
      "funding_type": "string",
      "provider": "string",
      "expected_amount": "string",
      "expected_decision_date": "date",
      "notes": "string",
      "stage": "string",
      "lost_reason": "string",
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
