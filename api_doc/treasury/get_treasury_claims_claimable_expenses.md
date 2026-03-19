# GET /treasury/claims/claimable-expenses

Get finished expenses claimable for a specific funding source.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_source_id | UUID | Yes | Funding source ID to find claimable expenses for |

**Response:**
```json
[
  {
    "id": "uuid",
    "expense_category_name": "Personnel",
    "total_value": 5000.00,
    "allocated_amount": 5000.00,
    "transaction_date": "2026-03-01",
    "note": "March payroll",
    "created_at": "2026-03-01T08:00:00+00:00"
  }
]
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 422 | Missing required `funding_source_id` parameter |
