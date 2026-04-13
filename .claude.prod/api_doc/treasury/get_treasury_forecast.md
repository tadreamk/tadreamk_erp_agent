# GET /treasury/forecast

Get a cash flow forecast for the specified number of months ahead. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| months | integer | No | Number of months to forecast (default: 6, min: 1, max: 12) |

**Response:** Array of monthly forecast data

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
