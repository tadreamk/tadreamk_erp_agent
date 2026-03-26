# GET /market-research/companies

List market research companies with optional filters. Requires `market-research` whitelist.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| industry | string | — | Filter by industry |
| tier | int (1-5) | — | Filter by potential tier |
| country | string | — | Filter by country |
| company_size | string | — | Filter by company size |
| search | string | — | Search by company name (ILIKE) |
| skip | int | 0 | Pagination offset |
| limit | int | 50 | Page size (max 100) |

**Response:** `MarketResearchListResponse[]`
```json
[
  {
    "id": "uuid",
    "slug": "company-slug",
    "name": "Company Name",
    "industry": "Technology",
    "location_city": "Hong Kong",
    "location_country": "HK",
    "company_size": "51-200",
    "potential_score": 12,
    "potential_tier": 4,
    "best_entry_points": [{"area": "...", "reason": "..."}],
    "has_jobs": true
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
