# GET /exercises/


List exercises with filtering and pagination. Returns an empty list (not `403`) when the caller lacks whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tags | string | No | -- | Comma-separated tag filter (e.g. `backend,llm`) |
| search | string | No | -- | Free-text search on exercise content/title |
| post_active | bool | No | -- | Filter by active status (`true`/`false`) |
| date_from | string | No | -- | ISO 8601 datetime lower bound |
| date_to | string | No | -- | ISO 8601 datetime upper bound |
| page | int | No | 1 | Page number (min 1) |
| limit | int | No | 20 | Items per page (1--100) |

**Response:**
```json
{
  "exercises": [
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
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 42,
    "total_pages": 3,
    "has_next": true,
    "has_prev": false
  },
  "filters": {
    "tags": ["backend", "llm"]
  }
}
```

**Errors:**
- `401` -- Not authenticated
