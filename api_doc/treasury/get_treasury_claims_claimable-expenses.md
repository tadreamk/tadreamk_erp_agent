# GET /treasury/claims/claimable-expenses

Get finished expenses that are claimable for a given funding source. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_source_id | UUID | Yes | The funding source to check claimable expenses for |

**Response:** Array of claimable expense objects

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
