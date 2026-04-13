# POST /bank-statements/{statement_id}/lines

Add a transaction line to a bank statement. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |

**Request Body:**
```json
{
  "transaction_date": "2025-08-01",
  "description": "Salary disbursement",
  "deposit_amount": null,
  "withdrawal_amount": 50000.00,
  "running_balance": 60000.00,
  "line_order": 0
}
```

At least one of `deposit_amount` or `withdrawal_amount` must be provided.

**Response:** `201` — Created line

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Statement not found
- `422` — Validation error (neither deposit nor withdrawal provided)
