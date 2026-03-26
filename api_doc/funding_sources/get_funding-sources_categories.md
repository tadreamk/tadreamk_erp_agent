# GET /funding-sources/categories

List all active expense categories (for filtering). Requires `funding-sources` whitelist.

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Travel",
    "description": "Travel expenses",
    "is_active": true,
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
