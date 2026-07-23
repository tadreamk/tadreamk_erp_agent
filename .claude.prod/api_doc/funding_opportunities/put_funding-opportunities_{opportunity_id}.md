# PUT /funding-opportunities/{opportunity_id}

Update Funding Opportunity. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| opportunity_name | string | No |  |
| funding_type | FundingTypeEnum | No |  |
| provider | string | No |  |
| expected_amount | number|string | No |  |
| expected_decision_date | string | No |  |
| notes | string | No |  |
| lost_reason | string | No |  |

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
