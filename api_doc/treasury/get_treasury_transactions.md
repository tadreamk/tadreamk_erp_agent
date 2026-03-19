# GET /treasury/transactions

List treasury transactions with optional filters and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| direction | string | No | Filter by direction: `inflow`, `outflow` |
| type | string | No | Filter by transaction type: `boss_injection`, `boss_withdrawal`, `expense_payment`, `funder_reimbursement` |
| date_from | string | No | Start date filter (ISO format: `YYYY-MM-DD`) |
| date_to | string | No | End date filter (ISO format: `YYYY-MM-DD`) |
| skip | int | No | Offset for pagination (default: 0) |
| limit | int | No | Items per page (default: 50, min: 1, max: 100) |

**Response:**
```json
[
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
]
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
