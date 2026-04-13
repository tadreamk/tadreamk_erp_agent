# GET /job-post/{job_post_id}/translations

Get all translations for a job post. Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | uuid | Yes | Job post ID |

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
  },
  "translation_status": "translated",
  "translated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
