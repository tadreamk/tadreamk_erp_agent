# PUT /admin/leave/entitlements/{entitlement_id}


Update an existing leave entitlement. All fields are optional; only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entitlement_id | UUID | Leave entitlement ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| from_date | date | No | New period start date |
| end_date | date | No | New period end date |
| amount | float | No | New entitlement amount (>= 0) |
| notes | string | No | Updated notes |

**Request example:**
```json
{
  "amount": 16.0,
  "notes": "Increased for senior employees"
}
```

**Response:**
```json
{
  "message": "Entitlement updated successfully",
  "entitlement": {
    "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "employee_username": "john.doe",
    "leave_type": "annual",
    "from_date": "2026-01-01",
    "end_date": "2026-12-31",
    "amount": 16.0,
    "notes": "Increased for senior employees",
    "created_at": "2026-01-01T00:00:00+00:00",
    "updated_at": "2026-03-12T11:00:00+00:00"
  }
}
```

**Errors:**
- `400` — Validation error (e.g., negative amount)
- `401` — Not authenticated
- `403` — Not an admin user
- `404` — Leave entitlement not found
