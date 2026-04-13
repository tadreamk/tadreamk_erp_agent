# GET /expense-categories

List expense categories. Requires `expense-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| include_inactive | bool | No | Include inactive categories (default: false) |

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Travel",
    "description": "Travel expenses",
    "is_active": true,
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
