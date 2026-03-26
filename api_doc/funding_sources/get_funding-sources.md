# GET /funding-sources

List all funding sources with optional filters. Requires `funding-sources` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by funding type |
| status | string | No | Filter by status |
| category_id | UUID | No | Filter by expense category |
| search | string | No | Search by name |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "source_name": "Grant ABC",
    "funding_type": "Grant",
    "provider": "Government",
    "total_approved": 100000.0,
    "status": "active",
    "start_date": "2025-01-01",
    "end_date": "2026-12-31",
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
