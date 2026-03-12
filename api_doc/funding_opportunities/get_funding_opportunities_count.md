# GET /funding-opportunities/count


Get count of funding opportunities matching optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by type: `government`, `corporate`, `internal`, `donation`, `investment` |
| status | string | No | Filter by status: `researching`, `submitted`, `awarded`, `rejected`, `expired`, `closed` |

**Response:**
```json
{
  "count": 8
}
```
