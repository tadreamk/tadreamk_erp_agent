# GET /user-requirements/{story_id}

Get Story. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| story_id | string |  |

**Response:**
```json
{
  "id": "string",
  "title": "string",
  "content": "string",
  "status": "string",
  "validation_instructions": "",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_by": "string",
  "updated_by_preferred_name": "string",
  "implemented_by": "string",
  "implemented_by_preferred_name": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "request_sent_at": "datetime",
  "in_development_at": "datetime",
  "ready_to_try_at": "datetime",
  "live_at": "datetime",
  "cancelled_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
