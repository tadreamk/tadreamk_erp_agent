# GET /funding-sources/count

Get count of funding sources with optional filters. Requires `funding-sources` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by funding type |
| status | string | No | Filter by status |
| category_id | UUID | No | Filter by expense category |

**Response:**
```json
{
  "count": 8
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
