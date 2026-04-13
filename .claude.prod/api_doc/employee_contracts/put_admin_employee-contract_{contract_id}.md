# PUT /admin/employee-contract/{contract_id}

Update an existing employee contract. Requires `employee-contracts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| contract_id | UUID | The contract's unique identifier |

**Request Body:** Same fields as POST /employee-contract/me (all optional)

**Response:**
```json
{
  "message": "Employee contract updated",
  "contract": { "...contract object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
- `404` — Contract not found
