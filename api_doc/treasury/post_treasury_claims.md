# POST /treasury/claims

Create a new funder claim in draft status.

**Request Body:**
```json
{
  "funding_source_id": "uuid",
  "expense_ids": ["uuid1", "uuid2"],
  "total_amount": 45000.00,
  "expected_date": "2026-04-15",
  "claim_reference": "CLM-2026-001",
  "note": "Q1 personnel expenses claim"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_source_id | UUID | Yes | Funding source to claim from |
| expense_ids | list[UUID] | Yes | List of expense IDs to include in claim |
| total_amount | float | Yes | Total claim amount (must be > 0) |
| expected_date | date | No | Expected payment date |
| claim_reference | string | No | External claim reference number |
| note | string | No | Optional note |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "status": "draft",
  "total_amount": 45000.00,
  "expense_ids": ["uuid1", "uuid2"],
  "created_by": "username",
  "created_at": "2026-03-18T08:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 422 | Validation error |
