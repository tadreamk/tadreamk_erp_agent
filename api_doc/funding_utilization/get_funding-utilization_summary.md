# GET /funding-utilization/summary

Get overall funding utilization summary. Requires `funding-sources` whitelist.

**Response:**
```json
{
  "total_approved": 500000.0,
  "utilized": 200000.0,
  "remaining": 300000.0,
  "utilization_percentage": 40.0
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
