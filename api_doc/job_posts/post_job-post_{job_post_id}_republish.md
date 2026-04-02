# POST /job-post/{job_post_id}/republish

Republish a closed job post. Changes status from closed back to published. Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:**
```json
{
  "message": "Job post republished successfully",
  "job_post": { "...job post object with status: published..." }
}
```

**Errors:**
- `400` — Only closed job posts can be republished
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
