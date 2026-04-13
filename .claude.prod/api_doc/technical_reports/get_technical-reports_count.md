# GET /technical-reports/count

Get the count of all technical reports. Requires `technical-reports` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by report status |
| search | string | No | Search by title or description |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on technical-reports whitelist
