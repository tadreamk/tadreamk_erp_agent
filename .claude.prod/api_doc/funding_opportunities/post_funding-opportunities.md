# POST /funding-opportunities

Create Funding Opportunity. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| opportunity_name | string | Yes |  |
| funding_type | FundingTypeEnum | Yes |  |
| provider | string | Yes |  |
| expected_amount | number|string | Yes |  |
| expected_decision_date | string | No |  |
| notes | string | No |  |
| stage | _FundingOpportunityStageOnCreateEnum | No |  |

**Response:**
```json
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
```

**Errors:**
- `422` — Validation Error
