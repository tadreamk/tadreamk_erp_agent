# GET /funding-sources/{source_id}/allocations


List all expense category allocations for a funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Response:**
```json
[
  {
    "id": "uuid",
    "funding_source_id": "uuid",
    "expense_category_id": "uuid",
    "expense_category_title": "Office Supplies",
    "expense_category_description": "General office supplies and stationery",
    "allocated_amount": 50000.00,
    "updated_by": "admin_user",
    "created_at": "2026-01-15T10:00:00",
    "updated_at": "2026-02-01T14:30:00",
    "is_active": true
  }
]
```

**Errors:**
- `404` -- Funding source not found
