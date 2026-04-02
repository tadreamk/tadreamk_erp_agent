# GET /funding-utilization/source/{funding_source_id}

Get detailed utilization for a specific funding source, including breakdown by category. Requires `funding-sources` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| funding_source_id | UUID | The funding source's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "source_name": "Grant ABC",
  "total_approved": 100000.0,
  "utilized": 40000.0,
  "remaining": 60000.0,
  "utilization_percentage": 40.0,
  "by_category": [
    {
      "category_name": "Travel",
      "allocated": 20000.0,
      "utilized": 10000.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
- `404` — Funding source not found
