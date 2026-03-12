# POST /job-post/{job_post_id}/publish


Publish a draft job post. Sets `published_at` timestamp.

**Errors:**
- `400` — Already published, or cannot publish a closed post
- `404` — Not found
