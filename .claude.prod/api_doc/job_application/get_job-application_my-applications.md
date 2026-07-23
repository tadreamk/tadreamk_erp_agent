# GET /job-application/my-applications

My Applications. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No |  |
| page_size | integer | No |  |

**Response:**
```json
{
  "items": [
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
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
