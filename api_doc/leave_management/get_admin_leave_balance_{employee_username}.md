# GET /admin/leave/balance/{employee_username}

Get leave balance for a specific employee. Requires `leave-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_username | string | The employee's username |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | Yes | Leave type (annual, sick, no_pay, maternal) |
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
- `403` — No leave-management whitelist access
