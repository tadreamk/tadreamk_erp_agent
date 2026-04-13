# GET /guide-pages

Get all active guide pages (without content for performance). Requires employee authentication.

**Response:**
```json
[
  {
    "id": "uuid",
    "slug": "getting-started",
    "title": "Getting Started",
    "section": "Onboarding",
    "sort_order": 1
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access guide pages
