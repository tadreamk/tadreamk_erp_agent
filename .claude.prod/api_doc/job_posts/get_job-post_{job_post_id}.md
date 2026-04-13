# GET /job-post/{job_post_id}

Get a specific job post by ID (all statuses). Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:** Full job post object

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
