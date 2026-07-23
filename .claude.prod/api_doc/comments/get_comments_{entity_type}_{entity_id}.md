# GET /comments/{entity_type}/{entity_id}

List Thread. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string |  |
| entity_id | string |  |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "string",
      "entity_type": "string",
      "entity_id": "string",
      "content": "string",
      "author_username": "string",
      "author_preferred_name": "string",
      "mentions": [
        "string"
      ],
      "file_urls": [
        {
          "file_url": {},
          "filename": {},
          "content_type": {},
          "size_bytes": {}
        }
      ],
      "is_deleted": false,
      "is_edited": false,
      "created_at": "datetime",
      "created_by": "string",
      "updated_at": "datetime",
      "updated_by": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
