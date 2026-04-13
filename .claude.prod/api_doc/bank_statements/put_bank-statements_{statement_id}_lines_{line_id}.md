# PUT /bank-statements/{statement_id}/lines/{line_id}

Edit a transaction line. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |
| line_id | UUID | Line ID |

**Request Body (all optional):**
```json
{
  "transaction_date": "2025-08-02",
  "description": "Updated description",
  "deposit_amount": 5000.00,
  "withdrawal_amount": null,
  "running_balance": 65000.00,
  "line_order": 1
}
```

**Response:** `200` — Updated line

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Line not found (or does not belong to this statement)
