# GET /customers/count


Get total count of customers matching the given filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| industry | string | No | Filter by industry |
| source | string | No | Filter by source |
| search | string | No | Search across customer fields |

**Response:**
```json
{
  "count": 128
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to customer management
