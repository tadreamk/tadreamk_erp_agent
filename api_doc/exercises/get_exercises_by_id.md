# GET /exercises/{slug}


Get a single exercise by its URL slug.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly exercise slug |

**Response:**
```json
{
  "id": "uuid",
  "slug": "exercise-title",
  "title": "Exercise Title",
  "tags": ["backend", "llm"],
  "content": "# Markdown content...",
  "post_active": true,
  "score_instruction_id": "uuid-or-null",
  "created_at": "2026-01-15T08:00:00+00:00",
  "updated_at": "2026-01-16T10:30:00+00:00",
  "created_by": "admin.user",
  "updated_by": "admin.user"
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- Access denied (user is not whitelisted and does not have this exercise assigned)
- `404` -- Exercise not found (or inactive and user is not whitelisted)
