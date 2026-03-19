# GET /treasury/transactions/{transaction_id}

Get a single treasury transaction by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| transaction_id | UUID | Transaction ID |

**Response:**
```json
{
  "id": "uuid",
  "transaction_type": "boss_injection",
  "direction": "inflow",
  "amount": 50000.00,
  "transaction_date": "2026-03-15",
  "note": "March funding",
  "expense_id": null,
  "funder_claim_id": null,
  "created_by": "username",
  "created_at": "2026-03-15T10:00:00+00:00",
  "updated_at": "2026-03-15T10:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Transaction not found |
