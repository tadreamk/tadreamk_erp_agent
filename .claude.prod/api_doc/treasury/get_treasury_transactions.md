# GET /treasury/transactions

List treasury transactions with optional filtering. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| direction | string | No | Filter by direction (`inflow` or `outflow`) |
| type | string | No | Filter by transaction type |
| date_from | string | No | Filter from date (ISO format: YYYY-MM-DD) |
| date_to | string | No | Filter to date (ISO format: YYYY-MM-DD) |
| skip | integer | No | Pagination offset (default: 0) |
| limit | integer | No | Max results (default: 50, max: 100) |

**Response:** Array of transaction objects

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
