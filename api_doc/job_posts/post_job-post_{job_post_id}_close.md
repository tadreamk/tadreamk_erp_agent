# POST /job-post/{job_post_id}/close

Close a published job post. Changes status from published to closed. Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:**
```json
{
  "message": "Job post closed successfully",
  "job_post": { "...job post object with status: closed..." }
}
```

**Errors:**
- `400` — Already closed or is draft (must publish first)
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
