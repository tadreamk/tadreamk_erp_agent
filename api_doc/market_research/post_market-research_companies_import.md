# POST /market-research/companies/import

Bulk upsert market research companies by slug. Existing companies (matched by slug) are updated; new slugs are inserted. Requires `market-research` whitelist.

**Request Body:**
```json
{
  "companies": [
    {
      "slug": "company-slug",
      "name": "Company Name",
      "industry": "Technology",
      "location_city": "Hong Kong",
      "location_country": "HK",
      "potential_score": 12,
      "potential_tier": 4
    }
  ]
}
```

All fields in each company object match the `MarketResearchImportItem` schema (same fields as the detail response, minus `id`, `created_at`, `updated_at`).

**Response:**
```json
{
  "created": 5,
  "updated": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
