# GET /bank-statements/count

Count active bank statements. Requires `bank-statements` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bank_account_id | UUID | No | Filter by bank account |
| year | int | No | Filter by statement year |

**Response:**
```json
{"count": 12}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
