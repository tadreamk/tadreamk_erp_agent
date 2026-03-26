# DELETE /job-post/{job_post_id}

Soft delete a job post (sets is_active=False). Requires `job_post` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Response:**
```json
{
  "message": "Job post deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job_post whitelist access
- `404` — Job post not found
