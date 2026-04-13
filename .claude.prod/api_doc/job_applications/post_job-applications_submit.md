# POST /job-applications/submit

Submit a new job application with a resume file upload. Requires authentication. Uses multipart/form-data.

**Request Body (multipart/form-data):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| job_post_id | string | Yes | Job post UUID |
| email | string | Yes | Applicant email |
| phone | string | Yes | Applicant phone |
| cover_letter | string | Yes | Cover letter text |
| family_name | string | No | Family/last name |
| given_name | string | No | Given/first name |
| linkedin_url | string | No | LinkedIn profile URL |
| portfolio_url | string | No | Portfolio URL |
| additional_info | string | No | Additional information |
| resume | file | Yes | Resume file (uploaded to GCP) |

**Response:**
```json
{
  "message": "Application submitted successfully",
  "success": true,
  "data": {
    "id": "uuid",
    "status": "submitted"
  }
}
```

**Errors:**
- `400` — Duplicate application for this job post
- `401` — Not authenticated
- `422` — Invalid form data
