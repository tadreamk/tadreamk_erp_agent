# GET /leave/my-balance

Get the current user's leave balances for all leave types (only returns types with entitlement > 0). Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reference_date | date | No | Reference date for calculation (default: today) |

**Response:**
```json
{
  "employee_username": "alice",
  "balances": [
    {
      "leave_type": "annual",
      "entitled": 14,
      "used": 4,
      "available": 10
    },
    {
      "leave_type": "sick",
      "monthly_limit": 4,
      "entitled": 4,
      "used": 1,
      "pending": 0,
      "available": 3,
      "is_monthly_limit": true,
      "contract_months": 24,
      "from_date": "2026-03-01",
      "end_date": "2026-03-31"
    }
  ]
}
```

**Note:** Sick leave balance uses `is_monthly_limit: true` with `monthly_limit` instead of flat entitlement. The limit is auto-calculated from contract duration: 2 days/month (first 12 months), 4 days/month (after 12 months).

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
