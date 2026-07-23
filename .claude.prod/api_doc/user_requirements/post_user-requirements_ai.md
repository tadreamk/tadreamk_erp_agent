# POST /user-requirements/ai

Ai Create. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| prompt | string | Yes |  |

**Response:**
```json
{
  "draft_title": "string",
  "draft_content": "string"
}
```

**Errors:**
- `422` — Validation Error
