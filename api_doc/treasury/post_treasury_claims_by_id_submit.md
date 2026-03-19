# POST /treasury/claims/{claim_id}/submit

Submit a draft claim to funder. Only draft claims can be submitted. Sends a notification to relevant users.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | Claim ID |

**Response:**
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "status": "submitted",
  "total_amount": 45000.00,
  "submitted_date": "2026-03-20T10:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Only draft claims can be submitted |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Claim not found |
