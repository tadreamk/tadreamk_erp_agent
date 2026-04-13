# GET /customers/count

Get count of customers with optional filters. Requires `customer-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | string | No | Filter by industry |
| source | string | No | Filter by customer source |
| search | string | No | Search by name or company |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
