# GET /market-research/companies/{slug}

Get a single market research company by slug. Requires `market-research` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly company identifier |

**Response:** `MarketResearchDetailResponse` — full company profile including all JSONB fields (strengths, weaknesses, IT/AI opportunities, etc.).

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
- `404` — Company not found
