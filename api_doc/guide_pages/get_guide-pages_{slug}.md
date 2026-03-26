# GET /guide-pages/{slug}

Get a single guide page by slug (includes full content). Requires employee authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The guide page's URL slug |

**Response:**
```json
{
  "id": "uuid",
  "slug": "getting-started",
  "title": "Getting Started",
  "section": "Onboarding",
  "content": "Full markdown/HTML content...",
  "sort_order": 1
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access guide pages
- `404` — Guide page not found
