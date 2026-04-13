# PUT /job-post/{job_post_id}

Update an existing job post. Requires `job-posts` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Request Body:** (all fields optional)
| Field | Type | Description |
|-------|------|-------------|
| title | string | Job post title |
| department | string | Department |
| job_type | string | Job type |
| location | string | Job location |
| job_slogan | string | Job slogan |
| about_us | string | About us section |
| experience | string | Required experience |
| application_deadline | date | Application deadline |
| description_en | string | Description (English) |
| responsibilities_en | string | Responsibilities (English) |
| requirements_en | string | Requirements (English) |
| benefits_en | string | Benefits (English) |
| preferred_qualifications_en | string | Preferred qualifications |
| translations | object | Translations by language code |
| translation_status | string | Translation status |

**Response:**
```json
{
  "message": "Job post updated successfully",
  "job_post": { "...job post object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
- `404` — Job post not found
