# PUT /guide-pages/admin/{page_id}

Update an existing guide page. Only provided fields are updated.

**Access:** Whitelist `guide-pages` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page_id | UUID | Guide page ID |

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "## Updated content...",
  "is_active": false
}
```

All fields are optional. Only provided fields are updated.

| Field | Type | Description |
|-------|------|-------------|
| slug | string | URL slug (1-100 chars) |
| title | string | Page title (1-255 chars) |
| section | string | Section grouping (1-100 chars) |
| content | string | Markdown content |
| sort_order | int | Display order |
| is_active | bool | Active status |

**Response:**
```json
{
  "id": "uuid",
  "slug": "onboarding-guide",
  "title": "Updated Title",
  "section": "HR",
  "content": "## Updated content...",
  "sort_order": 5,
  "is_active": false,
  "created_by": "username",
  "updated_by": "admin",
  "created_at": "2026-03-19T10:00:00+00:00",
  "updated_at": "2026-03-19T14:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Guide page not found |
