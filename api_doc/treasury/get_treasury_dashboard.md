# GET /treasury/dashboard

Get the treasury dashboard summary including balance, burn rate, runway, and pending receivables. Requires `expense-management` whitelist access.

**Response:**
```json
{
  "total_balance": 500000.00,
  "total_inflow": 800000.00,
  "total_outflow": 300000.00,
  "burn_rate_monthly": 25000.00,
  "runway_months": 20,
  "pending_receivables": 50000.00
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
