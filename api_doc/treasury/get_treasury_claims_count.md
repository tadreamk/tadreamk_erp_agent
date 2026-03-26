# GET /treasury/claims/count

Count funder claims with optional filtering. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_source_id | UUID | No | Filter by funding source |
| status | string | No | Filter by claim status |

**Response:**
```json
{
  "count": 15
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
