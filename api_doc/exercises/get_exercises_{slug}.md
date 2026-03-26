# GET /exercises/{slug}

Get an exercise by its slug. Access is granted if the user is admin/moderator OR has a job application with this exercise assigned.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The exercise's URL slug |

**Response:**
```json
{
  "id": "uuid",
  "slug": "exercise-slug",
  "title": "Exercise Title",
  "tags": ["tag1", "tag2"],
  "content": "Exercise content...",
  "created_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — You don't have access to this exercise
- `404` — Exercise not found
