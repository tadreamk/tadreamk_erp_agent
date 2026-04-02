# POST /treasury/transactions

Create a manual treasury transaction. Only `boss_injection` and `boss_withdrawal` types can be created manually; other types are auto-created by the system. Requires `expense-management` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amount | number | Yes | Transaction amount |
| transaction_type | string | Yes | `boss_injection` or `boss_withdrawal` |
| note | string | No | Transaction note |
| transaction_date | date | Yes | Date of transaction |

**Response:** `201 Created` — Transaction object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
