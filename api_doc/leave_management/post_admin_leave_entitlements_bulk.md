# POST /admin/leave/entitlements/bulk


Create the same leave entitlement for multiple employees at once.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_usernames | array of strings | Yes | List of employee usernames |
| leave_type | string | Yes | Leave type for all entitlements |
| from_date | date | Yes | Entitlement period start (YYYY-MM-DD) |
| end_date | date | Yes | Entitlement period end (YYYY-MM-DD) |
| amount | float | Yes | Number of days entitled (>= 0) |
| notes | string | No | Optional notes |

**Request example:**
```json
{
  "employee_usernames": ["john.doe", "jane.smith", "bob.jones"],
  "leave_type": "annual",
  "from_date": "2026-01-01",
  "end_date": "2026-12-31",
  "amount": 14.0,
  "notes": "2026 annual leave allocation"
}
```

**Response:**
```json
{
  "message": "Created 3 entitlements",
  "entitlements": [
    {
      "id": "d4e5f6a7-b890-1234-defg-567890123456",
      "employee_username": "john.doe",
      "leave_type": "annual",
      "from_date": "2026-01-01",
      "end_date": "2026-12-31",
      "amount": 14.0,
      "notes": "2026 annual leave allocation",
      "created_at": "2026-03-12T10:00:00+00:00",
      "updated_at": null
    },
    {
      "id": "e5f6a7b8-9012-3456-efgh-678901234567",
      "employee_username": "jane.smith",
      "...": "..."
    },
    {
      "id": "f6a7b890-1234-5678-fghi-789012345678",
      "employee_username": "bob.jones",
      "...": "..."
    }
  ]
}
```

**Errors:**
- `400` — Validation error
- `401` — Not authenticated
- `403` — Not an admin user
