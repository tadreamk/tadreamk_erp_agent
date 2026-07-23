# POST /user-requirements/{story_id}/ai-edit

Ai Prompt Edit. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| story_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| prompt | string | Yes |  |

**Response:**
```json
{
  "preview_content": "string"
}
```

**Errors:**
- `422` — Validation Error
