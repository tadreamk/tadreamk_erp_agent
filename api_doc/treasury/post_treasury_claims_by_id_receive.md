# POST /treasury/claims/{claim_id}/receive

Mark a submitted claim as received. Creates a treasury inflow transaction automatically. Sends a notification to relevant users.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | Claim ID |

**Request Body:**
```json
{
  "actual_amount": 44500.00,
  "received_date": "2026-04-10"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| actual_amount | float | Yes | Actual amount received (must be > 0) |
| received_date | date | Yes | Date payment was received |

**Response:**
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "status": "received",
  "total_amount": 45000.00,
  "actual_amount": 44500.00,
  "received_date": "2026-04-10",
  "updated_at": "2026-04-10T14:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Only submitted claims can be received |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Claim not found |
