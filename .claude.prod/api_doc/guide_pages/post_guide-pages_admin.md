# POST /guide-pages/admin

Create a new guide page. Requires `guide-pages` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| slug | string | Yes | URL slug (unique) |
| title | string | Yes | Page title |
| section | string | Yes | Section name (1-100 chars) |
| content | string | No | Page content (Markdown/HTML) |
| sort_order | int | No | Sort order within section |
| is_active | bool | No | Whether page is active (default: true) |

**Response:** Created guide page object (with all fields including is_active, created_by, etc.)

**Errors:**
- `401` — Not authenticated
- `403` — No guide-pages whitelist access
