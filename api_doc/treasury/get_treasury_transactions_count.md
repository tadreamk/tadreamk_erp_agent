# GET /treasury/transactions/count

Get count of treasury transactions matching optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| direction | string | No | Filter by direction: `inflow`, `outflow` |
| type | string | No | Filter by transaction type |

**Response:**
```json
{
  "count": 42
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
