# GET /funding-sources/count


Get count of funding sources matching optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_type | string | No | Filter by type: `government`, `corporate`, `internal`, `donation`, `investment` |
| status | string | No | Filter by status: `active`, `completed` |
| category_id | UUID | No | Filter by expense category ID |

**Response:**
```json
{
  "count": 12
}
```
