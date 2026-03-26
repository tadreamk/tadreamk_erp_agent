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
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
