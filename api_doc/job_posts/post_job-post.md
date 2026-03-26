# POST /job-post

Create a new job post. Created with status "draft". Requires `job_post` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Job post title |
| department | string | Yes | Department |
| job_type | string | Yes | Job type (full_time, part_time, contract, internship) |
| location | string | No | Job location |
| description_en | string | No | Description (English) |
| responsibilities_en | string | No | Responsibilities (English) |
| requirements_en | string | No | Requirements (English) |
| benefits_en | string | No | Benefits (English) |

**Response:**
```json
{
  "message": "Job post created successfully",
  "job_post": { "...job post object with status: draft..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job_post whitelist access
