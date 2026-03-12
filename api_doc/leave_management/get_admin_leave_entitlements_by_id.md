# GET /admin/leave/entitlements/{entitlement_id}


Get a single leave entitlement by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entitlement_id | UUID | Leave entitlement ID |

**Response:**
```json
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
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an admin user
- `404` — Leave entitlement not found
