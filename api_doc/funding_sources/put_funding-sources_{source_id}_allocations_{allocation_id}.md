# PUT /funding-sources/{source_id}/allocations/{allocation_id}

Update an expense category allocation amount. Validates total allocation does not exceed approved amount.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |
| allocation_id | UUID | The allocation's unique identifier |

**Auth:** Requires `funding-sources` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| allocated_amount | decimal | Yes | New amount to allocate (>= 0) |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "funding_source_id": "uuid",
  "expense_category_id": "uuid",
  "expense_category_title": "Travel",
  "expense_category_description": "Travel expenses",
  "allocated_amount": 75000.00,
  "updated_by": "admin",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-02T00:00:00",
  "is_active": true
}
```

**Errors:**
- `400` — Allocation does not belong to this funding source / Total allocation would exceed approved amount
- `401` — Not authenticated
- `403` — Not on funding-sources whitelist
- `404` — Funding source or allocation not found
