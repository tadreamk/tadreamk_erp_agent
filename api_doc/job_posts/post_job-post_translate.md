# POST /job-post/translate

Translate job post content from English to Chinese (preview without saving). Requires `job-posts` whitelist. Uses Gemini AI.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Job title to translate |
| job_slogan | string | No | Slogan to translate |
| description_en | string | No | Description in English |
| responsibilities_en | string | No | Responsibilities in English |
| requirements_en | string | No | Requirements in English |
| benefits_en | string | No | Benefits in English |
| preferred_qualifications_en | string | No | Preferred qualifications in English |
| about_us | string | No | About us section in English |

**Response:**
```json
{
  "translations": {
    "zh": {
      "title": "职位名称",
      "description": "..."
    },
    "zh-TW": {
      "title": "職位名稱",
      "description": "..."
    }
  }
}
```

**Errors:**
- `400` — Translation validation failed
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `500` — AI translation service error
