# POST /job-post/{job_post_id}/translate

Trigger background AI translation for a saved job post. Requires `job-posts` whitelist. Returns immediately; check `translation_status` for results.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | uuid | Yes | Job post ID |

**Response:**
```json
{
  "message": "Translation started",
  "job_post_id": "uuid",
  "translation_status": "translating"
}
```

**Translation Status Flow:**
- `translating` → `translated` (success) or `translation_failed` (failure)

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
