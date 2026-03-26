# GET /funding-opportunities/count

Get count of funding opportunities with optional filters. Requires `funding-opportunities` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by funding type |
| status | string | No | Filter by status |

**Response:**
```json
{
  "count": 12
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
