# GET /treasury/claims/{claim_id}

Get a single funder claim by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | Claim ID |

**Response:**
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "funding_source_name": "NSTC Grant",
  "status": "submitted",
  "total_amount": 45000.00,
  "actual_amount": null,
  "expected_date": "2026-04-15",
  "claim_reference": "CLM-2026-001",
  "note": "Q1 claim",
  "expense_ids": ["uuid1", "uuid2"],
  "submitted_date": "2026-03-20T10:00:00+00:00",
  "received_date": null,
  "created_by": "username",
  "created_at": "2026-03-18T08:00:00+00:00",
  "updated_at": "2026-03-20T10:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Claim not found |
