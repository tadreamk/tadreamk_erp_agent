# GET /funding-utilization/source/{funding_source_id}/expenses

Get recent expenses that used a specific funding source. Requires `funding-sources` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| funding_source_id | UUID | The funding source's unique identifier |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | int | No | Max results (default: 10, max: 50) |

**Response:**
```json
{
  "expenses": [
    {
      "id": "uuid",
      "title": "Conference Travel",
      "amount": 5000.0,
      "allocated_amount": 5000.0,
      "status": "finished",
      "expense_date": "2025-03-01"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
