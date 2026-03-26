# GET /exercises/

List all exercises with filtering and pagination. Requires `exercise` whitelist. Returns empty list if no access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tags | string | No | Comma-separated tags to filter by |
| search | string | No | Search in title/content |
| post_active | bool | No | Filter by active status |
| date_from | string | No | ISO date string for start range |
| date_to | string | No | ISO date string for end range |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 20, max: 100) |

**Response:**
```json
{
  "exercises": [
    {
      "id": "uuid",
      "slug": "exercise-slug",
      "title": "Exercise Title",
      "tags": ["JavaScript"],
      "post_active": true,
      "created_at": "datetime"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "total_pages": 3,
    "has_next": true,
    "has_prev": false
  },
  "filters": {}
}
```

**Errors:**
- `401` — Not authenticated
