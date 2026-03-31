# POST /bank-accounts

Create a new bank account. Requires `bank-statements` whitelist.

**Request Body:**
```json
{
  "bank_name": "Hang Seng Bank",
  "account_number": "242-462307-883",
  "currency": "HKD",
  "note": "Main operating account"
}
```

**Response:** `201`
```json
{
  "id": "uuid",
  "bank_name": "Hang Seng Bank",
  "account_number": "242-462307-883",
  "currency": "HKD",
  "note": "Main operating account",
  "is_active": true,
  "created_by": "alannguyen",
  "created_at": "datetime",
  "updated_at": null
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `422` — Validation error
