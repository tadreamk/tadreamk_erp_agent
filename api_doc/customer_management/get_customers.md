# GET /customers

List all customers with optional filters. Requires `customer-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | string | No | Filter by industry |
| source | string | No | Filter by customer source |
| search | string | No | Search by name or company |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

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
    "phone": "+1 555 1234",
    "industry": "Technology",
    "source": "Referral",
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
