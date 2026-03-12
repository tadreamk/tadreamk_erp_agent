# POST /funding-sources/{source_id}/allocations


Add an expense category allocation to a funding source. If a previously soft-deleted allocation exists for the same category, it will be reactivated with the new amount.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | Yes | ID of the expense category to allocate |
| allocated_amount | decimal | Yes | Amount to allocate to this category (>= 0) |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "expense_category_id": "uuid",
  "expense_category_title": "Office Supplies",
  "expense_category_description": "General office supplies and stationery",
  "allocated_amount": 50000.00,
  "updated_by": "admin_user",
  "created_at": "2026-02-10T09:00:00",
  "updated_at": null,
  "is_active": true
}
```

**Errors:**
- `400` -- This expense category is already allocated to this funding source
- `400` -- Total allocation would exceed approved amount. Available: {amount}
- `404` -- Funding source not found
- `404` -- Expense category not found
