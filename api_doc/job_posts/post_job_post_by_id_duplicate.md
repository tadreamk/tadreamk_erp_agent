# POST /job-post/{job_post_id}/duplicate


Duplicate an existing job post. Creates a copy with "[Copy]" prefix in title and status set to `draft`.

**Response:**
```json
{
  "message": "Job post duplicated successfully",
  "job_post": { "..." : "..." }
}
```

**Errors:**
- `404` — Job post not found

---

## Status Endpoints (Whitelist: job-posts)
