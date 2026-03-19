# GET /expense-categories

List expense categories. By default returns only active categories. Pass `include_inactive=true` to include deactivated categories.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| include_inactive | bool | No | Include inactive categories (default: false) |

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Personnel",
    "description": "Staff salaries and benefits",
    "is_active": true,
    "updated_by": "username",
    "created_at": "2026-01-01T00:00:00+00:00",
    "updated_at": "2026-01-01T00:00:00+00:00"
  }
]
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized (requires `expense-management` whitelist) |
