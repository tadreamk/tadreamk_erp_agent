# POST /treasury/transactions

Create a manual treasury transaction. Only `injection` and `withdrawal` types can be created manually; other types are auto-created by the system. Requires `expense-management` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amount | number | Yes | Transaction amount |
| direction | string | Yes | `inflow` or `outflow` |
| transaction_type | string | Yes | `injection` or `withdrawal` |
| description | string | No | Transaction description |
| transaction_date | date | No | Date of transaction (default: today) |

**Response:** `201 Created` — Transaction object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
