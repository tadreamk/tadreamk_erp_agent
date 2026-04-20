# GET /admin/employee-contract

List all employee contracts with optional filters. Requires `employee-contracts` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username or name |
| department | string | No | Filter by department |
| show_duplicates | boolean | No | If true, returns all contracts per employee (default: false = one per employee) |
| show_inactive | boolean | No | If true, includes inactive employees' contracts (default: false = active only) |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "contracts": [
    { "...contract object..." }
  ],
  "total": 25,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
