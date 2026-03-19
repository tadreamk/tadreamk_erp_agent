# POST /treasury/transactions

Create a manual treasury transaction (injection or withdrawal only).

**Request Body:**
```json
{
  "transaction_type": "boss_injection",
  "amount": 50000.00,
  "transaction_date": "2026-03-15",
  "note": "March capital injection"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| transaction_type | string | Yes | Must be `boss_injection` or `boss_withdrawal` |
| amount | float | Yes | Amount (must be > 0) |
| transaction_date | date | Yes | Date of the transaction |
| note | string | No | Optional note |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "transaction_type": "boss_injection",
  "direction": "inflow",
  "amount": 50000.00,
  "transaction_date": "2026-03-15",
  "note": "March capital injection",
  "created_by": "username",
  "created_at": "2026-03-15T10:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 422 | Validation error |
