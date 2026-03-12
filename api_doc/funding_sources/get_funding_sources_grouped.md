# GET /funding-sources/grouped


List all funding sources grouped by expense category.

**Response:**
```json
[
  {
    "category_id": "uuid",
    "category_title": "Office Supplies",
    "category_description": "General office supplies and stationery",
    "total_allocated": 150000.00,
    "sources": [
      {
        "id": "uuid",
        "source_name": "Government Grant 2026",
        "funding_type": "government",
        "total_approved": 500000.00,
        "allocated_amount": 150000.00
      }
    ]
  }
]
```
