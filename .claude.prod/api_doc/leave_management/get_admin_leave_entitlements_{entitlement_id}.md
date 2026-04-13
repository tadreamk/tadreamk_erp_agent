# GET /admin/leave/entitlements/{entitlement_id}

Get a specific leave entitlement. Requires admin authentication (head_of_hr or ceo).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| entitlement_id | uuid | Yes | Entitlement ID |

**Response:**
```json
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
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
- `404` — Entitlement not found
