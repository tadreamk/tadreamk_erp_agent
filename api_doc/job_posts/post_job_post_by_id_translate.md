# POST /job-post/{job_post_id}/translate


Trigger background AI translation for a job post. Returns immediately; status changes to `translating`, then `translated` on success or `translation_failed` on error.

**Response:**
```json
{
  "message": "Translation started",
  "job_post_id": "uuid",
  "translation_status": "translating"
}
```
