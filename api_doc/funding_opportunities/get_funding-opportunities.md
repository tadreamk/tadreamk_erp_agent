# GET /funding-opportunities

List all funding opportunities with optional filters. Requires `funding-opportunities` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by funding type |
| status | string | No | Filter by status |
| search | string | No | Search by name |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "opportunity_name": "Grant ABC",
    "funding_type": "Grant",
    "status": "open",
    "amount": 50000.0,
    "currency": "HKD",
    "deadline": "2026-06-30",
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
