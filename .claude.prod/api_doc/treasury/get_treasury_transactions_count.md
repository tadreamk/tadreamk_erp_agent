# GET /treasury/transactions/count

Count treasury transactions with optional filtering. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| direction | string | No | Filter by direction |
| type | string | No | Filter by transaction type |

**Response:**
```json
{
  "count": 150
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
