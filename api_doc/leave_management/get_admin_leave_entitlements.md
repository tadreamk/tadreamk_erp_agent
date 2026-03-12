# GET /admin/leave/entitlements


List all leave entitlements with optional filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| from_date | date | No | Filter entitlements starting from this date (YYYY-MM-DD) |
| end_date | date | No | Filter entitlements ending by this date (YYYY-MM-DD) |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "entitlements": [
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
  ],
  "total": 100,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an admin user
