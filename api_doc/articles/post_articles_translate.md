# POST /articles/translate


Translate article content via Gemini AI. Returns translations without saving.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Title to translate |
| summary | string | No | Summary to translate |
| content | string | No | Content to translate |
| target_languages | string[] | No | Language codes (default: `["zh", "zh-TW"]`) |

**Response:**
```json
{
  "translations": {
    "zh": { "title": "...", "summary": "...", "content": "..." },
    "zh-TW": { "title": "...", "summary": "...", "content": "..." }
  }
}
```

---

## Public Endpoints (No Authentication)
