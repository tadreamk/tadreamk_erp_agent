# GET /leave/my-balance/{leave_type}


Get the current user's leave balance for a specific leave type.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| leave_type | string | Leave type (`annual`, `sick`, `no_pay`, `maternal`, etc.) |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reference_date | date | No | Calculate balance as of this date (YYYY-MM-DD) |

**Response:**
```json
{
  "employee_username": "john.doe",
  "leave_type": "annual",
  "entitled": 14.0,
  "used": 3.0,
  "pending": 2.0,
  "available": 9.0,
  "from_date": "2026-01-01",
  "end_date": "2026-12-31"
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee record not found for current user
