# GET /guide-pages/admin

Get all guide pages including inactive ones. Requires `guide-pages` whitelist.

**Response:**
```json
[
  {
    "id": "uuid",
    "slug": "getting-started",
    "title": "Getting Started",
    "section": "Onboarding",
    "content": "...",
    "sort_order": 1,
    "is_active": true,
    "created_by": "string",
    "updated_by": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No guide-pages whitelist access
