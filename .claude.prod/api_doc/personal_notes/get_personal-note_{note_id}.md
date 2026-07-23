# GET /personal-note/{note_id}

Get Note. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| note_id | string |  |

**Response:**
```json
{
  "id": "string",
  "title": "string",
  "category": "string",
  "category_label": "string",
  "content_md": "string",
  "author_username": "string",
  "author_preferred_name": "string",
  "can_edit": false,
  "my_share": {
    "id": "string",
    "note_id": "string",
    "recipient_username": "string",
    "recipient_preferred_name": "string",
    "read_at": "datetime",
    "created_at": "datetime"
  },
  "shares": [
    {
      "id": "string",
      "note_id": "string",
      "recipient_username": "string",
      "recipient_preferred_name": "string",
      "read_at": "datetime",
      "created_at": "datetime"
    }
  ],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
