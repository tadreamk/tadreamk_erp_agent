# GET /guide-pages

List all active guide pages. Content is excluded for performance -- use the detail endpoint to fetch content.

**Access:** Authenticated employees only.

**Response:**
```json
[
  {
    "id": "uuid",
    "slug": "company-policies",
    "title": "Company Policies",
    "section": "General",
    "sort_order": 1
  }
]
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Only employees can access guide pages |
