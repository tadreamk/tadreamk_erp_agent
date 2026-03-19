# PUT /treasury/claims/{claim_id}

Update a draft or submitted claim. Received claims cannot be updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | Claim ID |

**Request Body:**
```json
{
  "expense_ids": ["uuid1", "uuid2", "uuid3"],
  "total_amount": 50000.00,
  "expected_date": "2026-04-20",
  "claim_reference": "CLM-2026-001-REV",
  "note": "Updated Q1 claim"
}
```

All fields are optional. Only provided fields are updated.

**Response:**
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "status": "draft",
  "total_amount": 50000.00,
  "updated_at": "2026-03-19T14:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Cannot update a received claim |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Claim not found |
