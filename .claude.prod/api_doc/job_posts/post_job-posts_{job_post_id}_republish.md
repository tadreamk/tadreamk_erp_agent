# POST /job-posts/{job_post_id}/republish

Republish Job Post. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "department": "string",
  "job_type": "string",
  "location": "string",
  "experience_years": 0,
  "application_deadline": "date",
  "content_by_lang": {},
  "status": "string",
  "published_at": "datetime",
  "closed_at": "datetime",
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
