# GET /funding-utilization/by-category


Get utilization totals grouped by expense category.

**Response:**
```json
{
  "categories": [
    {
      "category_id": "uuid",
      "category_name": "Salaries & Wages",
      "utilized": 450000.00,
      "percentage": 51.43
    },
    {
      "category_id": "uuid",
      "category_name": "Office Supplies",
      "utilized": 75000.00,
      "percentage": 8.57
    }
  ],
  "total_utilized": 875000.00
}
```
