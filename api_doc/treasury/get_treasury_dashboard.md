# GET /treasury/dashboard

Get treasury dashboard summary including current balance, totals, burn rate, runway, and pending receivables.

**Response:**
```json
{
  "current_balance": 150000.00,
  "total_injections": 500000.00,
  "total_withdrawals": 50000.00,
  "total_expense_payments": 280000.00,
  "total_reimbursements_received": 30000.00,
  "burn_rate_monthly": 25000.00,
  "runway_months": 6.0,
  "pending_receivables": 45000.00
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized (requires `expense-management` whitelist) |
