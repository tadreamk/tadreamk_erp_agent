# GET /admin/leave/entitlements/employee/{employee_username}


Get all leave entitlements for a specific employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_username | string | Employee's username |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| current_only | bool | No | If `true`, return only entitlements active as of today (default: `false`) |

**Response:**
```json
[
  {
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
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an admin user
