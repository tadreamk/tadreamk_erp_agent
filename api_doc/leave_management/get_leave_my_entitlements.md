# GET /leave/my-entitlements


Get the current user's leave entitlements.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| current_only | bool | No | If `true`, return only currently active entitlements (default: `false`) |

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
- `404` — Employee record not found for current user

---

## 32. Leave Amendment (Employee)

Endpoints for employees to request amendments (cancellation or date changes) to their already-approved leave requests.

**Prefix:** `/leave`
