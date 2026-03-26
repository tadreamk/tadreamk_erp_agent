# GET /funding-utilization/summary

Get overall funding utilization summary. Requires `funding-sources` whitelist.

**Response:**
```json
{
  "total_approved": 500000.0,
  "total_utilized": 200000.0,
  "total_remaining": 300000.0,
  "utilization_rate": 40.0,
  "sources_count": 5,
  "categories_count": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
