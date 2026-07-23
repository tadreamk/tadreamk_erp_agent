# GET /job-application/{workflow_id}/notes

List Notes. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "workflow_id": "uuid",
      "author_username": "string",
      "author_preferred_name": "string",
      "content": "string",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
