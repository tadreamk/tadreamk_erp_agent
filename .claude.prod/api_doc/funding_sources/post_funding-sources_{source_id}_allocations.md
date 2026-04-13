# POST /funding-sources/{source_id}/allocations

Add an expense category allocation to a funding source. Validates total allocation does not exceed approved amount.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Auth:** Requires `funding-sources` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | Yes | Expense category to allocate |
| allocated_amount | decimal | Yes | Amount to allocate (>= 0) |

**Response:** `201 Created`
```json
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
```

**Errors:**
- `400` — Category already allocated / Total allocation would exceed approved amount
- `401` — Not authenticated
- `403` — Not on funding-sources whitelist
- `404` — Funding source or expense category not found
