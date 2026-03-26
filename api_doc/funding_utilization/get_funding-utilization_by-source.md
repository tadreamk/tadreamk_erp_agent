# GET /funding-utilization/by-source

Get utilization breakdown for each funding source. Requires `funding-sources` whitelist.

**Response:**
```json
{
  "sources": [
    {
      "source_id": "uuid",
      "source_name": "Grant ABC",
      "total_approved": 100000.0,
      "total_utilized": 40000.0,
      "total_remaining": 60000.0,
      "utilization_rate": 40.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
