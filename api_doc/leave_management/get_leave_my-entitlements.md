# GET /leave/my-entitlements

Get the current user's leave entitlements. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| current_only | bool | No | Only show currently active entitlements (default: false) |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "alice",
    "leave_type": "annual",
    "amount": 14,
    "from_date": "2025-01-01",
    "end_date": "2025-12-31",
    "notes": "Annual leave entitlement",
    "created_at": "2025-01-01T00:00:00",
    "updated_at": "2025-01-01T00:00:00"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
