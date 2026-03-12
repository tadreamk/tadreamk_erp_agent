# POST /job-post/{job_post_id}/close


Close a published job post. Sets `closed_at` timestamp.

**Errors:**
- `400` — Already closed, or cannot close a draft
- `404` — Not found
