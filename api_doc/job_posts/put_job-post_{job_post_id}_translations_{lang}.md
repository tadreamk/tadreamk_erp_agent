# PUT /job-post/{job_post_id}/translations/{lang}

Update translation for a specific language. Requires `job_post` whitelist. Allows manual editing of AI-generated translations.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | uuid | Yes | Job post ID |
| lang | string | Yes | Language code: `zh` or `zh-TW` |

**Request Body:**
Translation fields as a JSON object (e.g., `{"title": "...", "description": "..."}`)

**Response:**
```json
{
  "message": "Translation for zh updated successfully",
  "job_post": {}
}
```

**Errors:**
- `400` — Invalid language code (only `zh` and `zh-TW` supported)
- `401` — Not authenticated
- `403` — No job_post whitelist access
- `404` — Job post not found
