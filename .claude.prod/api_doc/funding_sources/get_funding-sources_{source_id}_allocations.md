# GET /funding-sources/{source_id}/allocations

List all expense category allocations for a funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Auth:** Requires `funding-sources` whitelist access.

**Response:** `200 OK` — Array of allocation objects
```json
[
  {
    "id": "uuid",
    "funding_source_id": "uuid",
    "expense_category_id": "uuid",
    "expense_category_title": "Travel",
    "expense_category_description": "Travel expenses",
    "allocated_amount": 50000.00,
    "updated_by": "admin",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "is_active": true
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on funding-sources whitelist
- `404` — Funding source not found
