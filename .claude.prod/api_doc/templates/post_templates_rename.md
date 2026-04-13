# POST /templates/rename

Rename a template by its current title and category. Admin only.

Finds an active template matching the given title and category, then updates its title.

**Authentication:** Admin or moderator role required.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Current template title |
| category | string | Yes | Template category |
| new_title | string | Yes | New template title |

**Example Request:**
```json
{
  "title": "Full-time Employment Contract",
  "category": "contract",
  "new_title": "Full-time RTH Employment Contract"
}
```

**Response:** Returns the updated template object (same shape as `GET /templates/{template_id}`).

**Errors:**
- `401` — Not authenticated
- `403` — Not admin/moderator
- `404` — Template with given title/category not found
