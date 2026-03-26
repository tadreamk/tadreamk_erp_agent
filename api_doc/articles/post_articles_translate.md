# POST /articles/translate

Translate article content to target languages via Gemini AI.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Article title to translate |
| summary | string | No | Article summary to translate |
| content | string | No | Article content to translate |
| target_languages | list[string] | Yes | Languages to translate to (e.g., `["zh", "zh-TW"]`) |

**Response:**
```json
{
  "translations": {
    "zh": {
      "title": "string",
      "summary": "string",
      "content": "string"
    },
    "zh-TW": {
      "title": "string",
      "summary": "string",
      "content": "string"
    }
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to articles
