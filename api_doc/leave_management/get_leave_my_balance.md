# GET /leave/my-balance


Get the current user's leave balances across all leave types. Only types with entitlements (entitled > 0) are returned.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reference_date | date | No | Calculate balance as of this date (YYYY-MM-DD, default: today) |

**Response:**
```json
{
  "employee_username": "john.doe",
  "balances": [
    {
      "leave_type": "annual",
      "entitled": 14.0,
      "used": 3.0,
      "pending": 2.0,
      "available": 9.0,
      "from_date": "2026-01-01",
      "end_date": "2026-12-31"
    },
    {
      "leave_type": "sick",
      "entitled": 10.0,
      "used": 1.0,
      "pending": 0.0,
      "available": 9.0,
      "from_date": "2026-01-01",
      "end_date": "2026-12-31"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee record not found for current user
