# GET /admin/leave/entitlements

Get all leave entitlements with filtering. Requires admin authentication (head_of_hr or ceo).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| from_date | date | No | Filter by from date |
| end_date | date | No | Filter by end date |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "entitlements": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "leave_type": "annual",
      "amount": 14.0,
      "from_date": "2026-01-01",
      "end_date": "2026-12-31",
      "notes": null,
      "created_at": "datetime"
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
