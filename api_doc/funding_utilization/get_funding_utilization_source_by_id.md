# GET /funding-utilization/source/{funding_source_id}


Get detailed utilization for a specific funding source, including a breakdown by expense category.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| funding_source_id | UUID | Funding source ID |

**Response:**
```json
{
  "id": "uuid",
  "source_name": "Government Grant 2026",
  "funding_type": "government",
  "total_approved": 500000.00,
  "utilized": 320000.00,
  "remaining": 180000.00,
  "utilization_percentage": 64.00,
  "by_category": [
    {
      "category_id": "uuid",
      "category_name": "Salaries & Wages",
      "utilized": 200000.00,
      "percentage_of_utilized": 62.50
    },
    {
      "category_id": "uuid",
      "category_name": "Equipment",
      "utilized": 120000.00,
      "percentage_of_utilized": 37.50
    }
  ]
}
```

**Errors:**
- `404` -- Funding source not found
