# PUT /expenses/{expense_id}/allocation


Update the funding allocation for an expense. Specifies which funding sources cover the expense and how much from each.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_allocation | array | Yes | List of funding source allocations |

Each item in `funding_allocation`:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_sources_id | UUID | Yes | ID of the funding source |
| value | decimal | Yes | Amount allocated from this source (>= 0) |

**Request Example:**
```json
{
  "funding_allocation": [
    { "funding_sources_id": "uuid-1", "value": 3000.00 },
    { "funding_sources_id": "uuid-2", "value": 2000.00 }
  ]
}
```

**Response:** Updated expense object.

**Errors:**
- `404` -- Expense not found
