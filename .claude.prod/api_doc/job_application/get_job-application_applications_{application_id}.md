# GET /job-application/applications/{application_id}

Get Application For Candidate. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "job_post_id": "uuid",
  "job_post_title": "string",
  "username": "string",
  "username_preferred_name": "string",
  "family_name": "string",
  "given_name": "string",
  "email": "string",
  "phone": "string",
  "linkedin_url": "string",
  "portfolio_url": "string",
  "resume_url": "string",
  "cover_letter": "string",
  "additional_info": "string",
  "created_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
