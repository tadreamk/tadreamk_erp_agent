# POST /admin/leave/entitlements


Create a new leave entitlement for a single employee.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_username | string | Yes | Employee's username |
| leave_type | string | Yes | One of: `annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work` |
| from_date | date | Yes | Entitlement period start (YYYY-MM-DD) |
| end_date | date | Yes | Entitlement period end (YYYY-MM-DD), must be >= from_date |
| amount | float | Yes | Number of days entitled (>= 0) |
| notes | string | No | Optional notes |

**Request example:**
```json
{
  "employee_username": "john.doe",
  "leave_type": "annual",
  "from_date": "2026-01-01",
  "end_date": "2026-12-31",
  "amount": 14.0,
  "notes": "Standard annual entitlement"
}
```

**Response:**
```json
{
  "message": "Entitlement created successfully",
  "entitlement": {
    "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "employee_username": "john.doe",
    "leave_type": "annual",
    "from_date": "2026-01-01",
    "end_date": "2026-12-31",
    "amount": 14.0,
    "notes": "Standard annual entitlement",
    "created_at": "2026-01-01T00:00:00+00:00",
    "updated_at": null
  }
}
```

**Errors:**
- `400` — Validation error (e.g., end_date before from_date, negative amount)
- `401` — Not authenticated
- `403` — Not an admin user
