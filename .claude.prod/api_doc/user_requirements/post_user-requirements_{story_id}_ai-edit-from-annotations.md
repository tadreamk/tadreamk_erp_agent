# POST /user-requirements/{story_id}/ai-edit-from-annotations

Ai Annotation Edit. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| story_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| annotation_ids | array[string] | Yes |  |

**Response:**
```json
{
  "preview_content": "string",
  "ai_replies": [
    {
      "annotation_id": "uuid",
      "reply_text": "string"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
