# GET /admin/employee-contract

List all employee contracts with optional filters. Requires `employee-contracts` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username or name |
| department | string | No | Filter by department |
| offset | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 200) |

**Response:**
```json
{
  "contracts": [
    { "...contract object..." }
  ],
  "total": 25
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
