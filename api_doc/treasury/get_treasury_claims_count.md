# GET /treasury/claims/count

Get count of funder claims matching optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_source_id | UUID | No | Filter by funding source |
| status | string | No | Filter by claim status: `draft`, `submitted`, `received` |

**Response:**
```json
{
  "count": 12
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
