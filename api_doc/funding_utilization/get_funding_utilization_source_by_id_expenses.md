# GET /funding-utilization/source/{funding_source_id}/expenses


Get recent expenses that have been allocated from a specific funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| funding_source_id | UUID | Funding source ID |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | int | No | Number of expenses to return (default: 10, min: 1, max: 50) |

**Response:**
```json
{
  "expenses": [
    {
      "id": "uuid",
      "created_at": "2026-03-01T14:30:00",
      "category_name": "Office Supplies",
      "note": "Q1 stationery purchase",
      "allocated_amount": 2500.00
    },
    {
      "id": "uuid",
      "created_at": "2026-02-28T09:15:00",
      "category_name": "Salaries & Wages",
      "note": null,
      "allocated_amount": 45000.00
    }
  ]
}
```
