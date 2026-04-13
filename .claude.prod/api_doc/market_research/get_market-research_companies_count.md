# GET /market-research/companies/count

Get filtered count of market research companies. Requires `market-research` whitelist.

**Query Parameters:** Same as GET /market-research/companies (except skip, limit).

**Response:**
```json
{
  "count": 182
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
