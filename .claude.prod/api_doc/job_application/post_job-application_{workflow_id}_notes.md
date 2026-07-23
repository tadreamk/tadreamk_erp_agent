# POST /job-application/{workflow_id}/notes

Create Note. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes |  |
| mentioned_users | array[string] | No |  |

**Response:**
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "author_username": "string",
  "author_preferred_name": "string",
  "content": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
