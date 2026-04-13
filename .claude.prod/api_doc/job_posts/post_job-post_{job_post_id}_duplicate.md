# POST /job-post/{job_post_id}/duplicate

Duplicate a job post. Creates a copy with "[Copy]" prefix in the title and status set to draft. Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:**
```json
{
  "message": "Job post duplicated successfully",
  "job_post": { "...new job post object with status: draft..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
