# GET /funding-opportunities/{opportunity_id}

Get Funding Opportunity. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | string |  |

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
