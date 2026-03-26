# GET /market-research/companies/stats

Get aggregated dashboard statistics. Requires `market-research` whitelist.

**Response:**
```json
{
  "total": 182,
  "avg_score": 8.3,
  "tier_distribution": {"1": 20, "2": 35, "3": 60, "4": 45, "5": 22},
  "industry_distribution": {"Technology": 50, "Biotechnology": 30, "...": "..."}
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
