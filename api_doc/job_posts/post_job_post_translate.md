# POST /job-post/translate


Preview translation without saving. Uses Gemini AI to translate to zh and zh-TW.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Title in English |
| job_slogan | string | No | Slogan in English |
| about_us | string | No | About us in English |
| description_en | string | No | Description in English |
| responsibilities_en | string[] | No | Responsibilities |
| requirements_en | string[] | No | Requirements |
| benefits_en | string[] | No | Benefits |
| preferred_qualifications_en | string[] | No | Preferred qualifications |

**Response:**
```json
{
  "translations": {
    "zh": { "title": "...", "description_en": "...", "..." : "..." },
    "zh-TW": { "title": "...", "description_en": "...", "..." : "..." }
  }
}
```

**Errors:**
- `400` — Validation failed
- `500` — AI service error
