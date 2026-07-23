# PUT /exercises/{exercise_id}

Update Exercise. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| content | string | Yes |  |
| tag_ids | array[string] | No |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "content": "string",
  "status": "string",
  "tags": [
    {
      "id": "uuid",
      "name": "string",
      "status": "string"
    }
  ],
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "updated_at": "datetime",
  "updated_by": "string"
}
```

**Errors:**
- `422` — Validation Error
