# GET /customers


List all customers with optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | string | No | Filter by industry: `Technology`, `Finance`, `Healthcare`, `Manufacturing`, `Retail`, `Education`, `Real Estate`, `Professional Services`, `Hospitality`, `Logistics`, `Other` |
| source | string | No | Filter by source: `Referral`, `Website`, `Cold Call`, `Event`, `Advertisement`, `Partner`, `Social Media`, `Other` |
| search | string | No | Search across customer fields |
| skip | int | No | Offset for pagination (default: 0, min: 0) |
| limit | int | No | Max items to return (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Mr.",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Acme Corp",
    "email": "john@acme.com",
    "phone": "+1-555-0100",
    "industry": "Technology",
    "source": "Referral",
    "created_at": "2025-08-01T10:00:00Z"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to customer management
