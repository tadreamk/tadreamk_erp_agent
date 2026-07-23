# PUT /job-application/{workflow_id}/notes/{note_id}

Update Note. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string |  |
| note_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes |  |

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
