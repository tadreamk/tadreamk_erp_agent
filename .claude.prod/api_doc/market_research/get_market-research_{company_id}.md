# GET /market-research/{company_id}

Get Company. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| company_id | string |  |

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
