# POST /admin/employee-contract

Create a new employee contract for a specified user. Requires `employee-contracts` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Username to create contract for |

**Request Body:** Same fields as POST /employee-contract/me

**Response:**
```json
{
  "message": "Employee contract created",
  "contract": { "...contract object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
