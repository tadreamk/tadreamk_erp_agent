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

**Response (standard leave types):**
```json
{
  "employee_username": "alice",
  "leave_type": "annual",
  "entitled": 14,
  "used": 4,
  "available": 10
}
```

**Response (sick leave — monthly limit):**
```json
{
  "employee_username": "alice",
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
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
