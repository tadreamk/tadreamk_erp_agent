# PUT /bank-statements/{statement_id}

Update a bank statement header. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |

**Request Body (all optional):**
```json
{
  "statement_date": "2025-08-31",
  "opening_balance": 10000.00,
  "closing_balance": 12500.00,
  "note": "Updated note"
}
```

**Response:** `200` — Updated statement header

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Statement not found
