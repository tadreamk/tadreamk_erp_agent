# PUT /market-research/{company_id}

Update Company. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| company_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | No |  |
| industry | string | No |  |
| location_city | string | No |  |
| location_country | string | No |  |
| company_size | string | No |  |
| potential_score | integer | No |  |
| potential_score_reason | string | No |  |
| strengths | array[string] | No |  |
| weaknesses | array[string] | No |  |
| it_ai_service_opportunities | array[OpportunityItem] | No |  |
| best_entry_points | array[EntryPointItem] | No |  |
| note | string | No |  |
| scraped_at | string | No |  |

**Response:**
```json
{
  "id": "uuid",
  "name": "string",
  "industry": "string",
  "location_city": "string",
  "location_country": "string",
  "company_size": "string",
  "potential_score": 0,
  "potential_tier": 0,
  "potential_score_reason": "string",
  "strengths": [
    "string"
  ],
  "weaknesses": [
    "string"
  ],
  "it_ai_service_opportunities": [
    {
      "area": "string",
      "detail": "string"
    }
  ],
  "best_entry_points": [
    {
      "area": "string",
      "reason": "string"
    }
  ],
  "note": "string",
  "scraped_at": "date",
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
