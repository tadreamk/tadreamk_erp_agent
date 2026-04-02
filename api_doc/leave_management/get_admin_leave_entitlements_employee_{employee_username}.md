# GET /admin/leave/entitlements/employee/{employee_username}

Get entitlements for a specific employee. Requires admin authentication (head_of_hr or ceo).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_username | string | Yes | Employee username |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| current_only | bool | No | Return only currently active entitlements (default: false) |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john_doe",
    "leave_type": "annual",
    "amount": 14.0,
    "from_date": "2026-01-01",
    "end_date": "2026-12-31",
    "notes": null,
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
