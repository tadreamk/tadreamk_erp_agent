# GET /funding-utilization/by-category

Get funding utilization grouped by expense category. Requires `funding-sources` whitelist.

**Response:**
```json
{
  "categories": [
    {
      "category_id": "uuid",
      "category_title": "Travel",
      "total_allocated": 50000.0,
      "total_utilized": 20000.0,
      "utilization_rate": 40.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
