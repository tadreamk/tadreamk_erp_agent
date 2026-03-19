# GET /guide-pages/admin

List all guide pages including inactive ones. Returns all fields for admin management.

**Access:** Whitelist `guide-pages` required.

**Response:**
```json
[
  {
    "id": "uuid",
    "slug": "company-policies",
    "title": "Company Policies",
    "section": "General",
    "content": "## Overview\n\nMarkdown content...",
    "sort_order": 1,
    "is_active": true,
    "created_by": "username",
    "updated_by": "username",
    "created_at": "2026-01-15T08:00:00+00:00",
    "updated_at": "2026-02-20T14:00:00+00:00"
  }
]
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized (requires `guide-pages` whitelist) |
