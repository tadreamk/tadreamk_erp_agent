# GET /funding-opportunities


List all funding opportunities with optional filters and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by type: `government`, `corporate`, `internal`, `donation`, `investment` |
| status | string | No | Filter by status: `researching`, `submitted`, `awarded`, `rejected`, `expired`, `closed` |
| search | string | No | Search text |
| skip | int | No | Offset for pagination (default: 0, min: 0) |
| limit | int | No | Items per page (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "opportunity_name": "Innovation Fund 2026",
    "funding_type": "government",
    "provider": "National Science Council",
    "estimated_amount": 250000.00,
    "application_deadline": "2026-06-30",
    "status": "researching",
    "created_at": "2026-02-01T10:00:00"
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to funding opportunities management
