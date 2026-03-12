# POST /job-post/{job_post_id}/republish


Republish a closed job post. Updates `published_at` and clears `closed_at`.

**Errors:**
- `400` — Only closed posts can be republished
- `404` — Not found

---

## Translation Endpoints (Whitelist: job-posts)
