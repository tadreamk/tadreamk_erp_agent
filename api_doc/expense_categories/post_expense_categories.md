# POST /expense-categories

Create a new expense category. The title must be unique across all categories.

**Request Body:**
```json
{
  "title": "Equipment",
  "description": "Hardware and software purchases"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Category title (must be unique) |
| description | string | No | Category description |

**Response:**
```json
{
  "id": "uuid",
  "title": "Equipment",
  "description": "Hardware and software purchases",
  "is_active": true,
  "updated_by": "username",
  "created_at": "2026-03-19T10:00:00+00:00",
  "updated_at": "2026-03-19T10:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | A category with this title already exists |
| 401 | Not authenticated |
| 403 | Not authorized |
