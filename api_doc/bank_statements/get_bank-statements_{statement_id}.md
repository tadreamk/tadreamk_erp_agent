# GET /bank-statements/{statement_id}

Get a bank statement with all its transaction lines. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |

**Response:**
```json
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
  "updated_at": null,
  "lines": [
    {
      "id": "uuid",
      "bank_statement_id": "uuid",
      "transaction_date": "2025-08-01",
      "description": "Salary disbursement",
      "deposit_amount": null,
      "withdrawal_amount": "50000.00",
      "running_balance": "60000.00",
      "line_order": 0,
      "created_at": "datetime",
      "updated_at": null
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Statement not found
