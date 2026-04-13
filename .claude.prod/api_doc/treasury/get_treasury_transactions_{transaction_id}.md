# GET /treasury/transactions/{transaction_id}

Get a single treasury transaction by ID. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| transaction_id | UUID | The transaction's unique identifier |

**Response:** Transaction object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Transaction not found
