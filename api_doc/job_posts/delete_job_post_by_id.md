# DELETE /job-post/{job_post_id}


Soft delete a job post (sets `is_active=false`).

**Response:**
```json
{ "message": "Job post deleted successfully" }
```

**Errors:**
- `404` — Job post not found
