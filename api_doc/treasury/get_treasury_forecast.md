# GET /treasury/forecast

Get cash flow forecast for upcoming months.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| months | int | No | Number of months to forecast (default: 6, min: 1, max: 12) |

**Response:**
```json
{
  "starting_balance": 150000.00,
  "burn_rate_monthly": 25000.00,
  "months": [
    {
      "month": "2026-04",
      "projected_outflow": 25000.00,
      "expected_inflow": 10000.00,
      "projected_balance": 135000.00
    }
  ]
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
