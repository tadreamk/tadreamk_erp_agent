# GET /funding-utilization/by-source


Get utilization for each individual funding source.

**Response:**
```json
{
  "sources": [
    {
      "id": "uuid",
      "source_name": "Government Grant 2026",
      "funding_type": "government",
      "status": "active",
      "total_approved": 500000.00,
      "utilized": 320000.00,
      "remaining": 180000.00,
      "utilization_percentage": 64.00
    },
    {
      "id": "uuid",
      "source_name": "Corporate Sponsorship",
      "funding_type": "corporate",
      "status": "active",
      "total_approved": 1000000.00,
      "utilized": 555000.00,
      "remaining": 445000.00,
      "utilization_percentage": 55.50
    }
  ]
}
```
