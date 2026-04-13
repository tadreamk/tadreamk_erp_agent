# GET /bank-statements

List bank statements with optional filters. Requires `bank-statements` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bank_account_id | UUID | No | Filter by bank account |
| year | int | No | Filter by statement year |
| month | int | No | Filter by statement month |
| skip | int | No | Pagination offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "bank_account_id": "uuid",
    "bank_name": "Hang Seng Bank",
    "account_number": "242-462307-883",
    "statement_year": 2025,
    "statement_month": 8,
    "statement_date": "2025-08-31",
    "opening_balance": "10000.00",
    "closing_balance": "12500.00",
    "note": null,
    "created_by": "alannguyen",
    "created_at": "datetime",
    "updated_at": null
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
