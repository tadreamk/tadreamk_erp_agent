# GET /guide-pages/{slug}

Get a single guide page by slug, with full content.

**Access:** Authenticated employees only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL slug of the guide page |

**Response:**
```json
{
  "id": "uuid",
  "slug": "company-policies",
  "title": "Company Policies",
  "section": "General",
  "content": "## Overview\n\nMarkdown content here...",
  "sort_order": 1
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Only employees can access guide pages |
| 404 | Guide page not found (or inactive) |
