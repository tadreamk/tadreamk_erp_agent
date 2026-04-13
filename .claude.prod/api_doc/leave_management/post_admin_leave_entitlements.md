# POST /admin/leave/entitlements

Create a new leave entitlement. Requires admin authentication (head_of_hr or ceo).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_username | string | Yes | Employee username |
| leave_type | string | Yes | Leave type (annual, sick, etc.) |
| amount | float | Yes | Entitlement amount in days |
| from_date | date | Yes | Start date |
| end_date | date | Yes | End date |
| notes | string | No | Optional notes |

**Response:**
```json
{
  "message": "Entitlement created successfully",
  "entitlement": {
    "id": "uuid",
    "employee_username": "john_doe",
    "leave_type": "annual",
    "amount": 14.0,
    "from_date": "2026-01-01",
    "end_date": "2026-12-31"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
