# POST /bank-statements

Create a new bank statement header. Requires `bank-statements` whitelist.

**Request Body:**
```json
{
  "bank_account_id": "uuid",
  "statement_year": 2025,
  "statement_month": 8,
  "statement_date": "2025-08-31",
  "opening_balance": 10000.00,
  "closing_balance": 12500.00,
  "note": "August statement"
}
```

**Response:** `201` — Created statement header with `bank_name` and `account_number`

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `409` — Statement for this account and period already exists
- `422` — Validation error
