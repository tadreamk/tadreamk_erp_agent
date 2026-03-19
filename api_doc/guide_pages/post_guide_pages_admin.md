# POST /guide-pages/admin

Create a new guide page.

**Access:** Whitelist `guide-pages` required.

**Request Body:**
```json
{
  "slug": "onboarding-guide",
  "title": "Onboarding Guide",
  "section": "HR",
  "content": "## Welcome\n\nWelcome to the team...",
  "sort_order": 5,
  "is_active": true
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| slug | string | Yes | URL slug (1-100 chars, must be unique) |
| title | string | Yes | Page title (1-255 chars) |
| section | string | Yes | Section grouping (1-100 chars) |
| content | string | No | Markdown content (default: empty) |
| sort_order | int | No | Display order within section (default: 0) |
| is_active | bool | No | Whether page is active (default: true) |

**Response:**
```json
{
  "id": "uuid",
  "slug": "onboarding-guide",
  "title": "Onboarding Guide",
  "section": "HR",
  "content": "## Welcome\n\nWelcome to the team...",
  "sort_order": 5,
  "is_active": true,
  "created_by": "username",
  "updated_by": null,
  "created_at": "2026-03-19T10:00:00+00:00",
  "updated_at": null
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 422 | Validation error |
