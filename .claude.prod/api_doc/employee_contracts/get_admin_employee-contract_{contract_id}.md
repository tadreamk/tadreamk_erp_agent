# GET /admin/employee-contract/{contract_id}

Get a single employee contract by ID. Requires `employee-contracts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| contract_id | UUID | The contract's unique identifier |

**Response:** Contract object

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
- `404` — Contract not found
