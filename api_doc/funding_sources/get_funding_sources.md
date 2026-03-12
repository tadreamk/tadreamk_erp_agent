# GET /funding-sources


List all funding sources with optional filters and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by type: `government`, `corporate`, `internal`, `donation`, `investment` |
| status | string | No | Filter by status: `active`, `completed` |
| category_id | UUID | No | Filter by expense category ID |
| search | string | No | Search text |
| skip | int | No | Offset for pagination (default: 0, min: 0) |
| limit | int | No | Items per page (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "source_name": "Government Grant 2026",
    "funding_type": "government",
    "provider": "Ministry of Finance",
    "total_approved": 500000.00,
    "start_date": "2026-01-01",
    "end_date": "2026-12-31",
    "status": "active",
    "created_at": "2026-01-10T08:00:00",
    "is_active": true
  }
]
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to funding sources management
