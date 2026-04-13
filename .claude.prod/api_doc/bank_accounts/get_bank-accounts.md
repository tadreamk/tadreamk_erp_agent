# GET /bank-accounts

List all active bank accounts. Requires `bank-statements` whitelist.

**Response:**
```json
[
  {
    "id": "uuid",
    "bank_name": "Hang Seng Bank",
    "account_number": "242-462307-883",
    "currency": "HKD",
    "note": null,
    "is_active": true,
    "created_by": "alannguyen",
    "created_at": "datetime",
    "updated_at": null
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
