# POST /job-post/{job_post_id}/publish

Publish a draft job post. Changes status from draft to published. Requires `job_post` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:**
```json
{
  "message": "Job post published successfully",
  "job_post": { "...job post object with status: published..." }
}
```

**Errors:**
- `400` — Already published or is closed
- `401` — Not authenticated
- `403` — No job_post whitelist access
- `404` — Job post not found
