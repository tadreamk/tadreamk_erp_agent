# GET /personal-note

List Notes. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No |  |
| q | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "string",
      "title": "string",
      "category": "string",
      "category_label": "string",
      "author_username": "string",
      "author_preferred_name": "string",
      "shared_with": [
        {
          "username": {},
          "preferred_name": {}
        }
      ],
      "is_mine": false,
      "is_unread": false,
      "updated_at": "datetime",
      "created_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
