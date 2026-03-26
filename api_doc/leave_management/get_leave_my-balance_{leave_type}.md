# GET /leave/my-balance/{leave_type}

Get the current user's leave balance for a specific leave type. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| leave_type | string | Leave type (annual, sick, no_pay, maternal) |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reference_date | date | No | Reference date for calculation (default: today) |

**Response:**
```json
{
  "employee_username": "alice",
  "leave_type": "annual",
  "entitled": 14,
  "used": 4,
  "available": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
