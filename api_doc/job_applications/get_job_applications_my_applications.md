# GET /job-applications/my-applications


Get all applications submitted by the currently authenticated user. Paginated.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| skip | int | No | 0 | Number of records to skip |
| limit | int | No | 20 | Maximum number of records to return |

**Response (200):**
```json
{
  "applications": [
    {
      "id": "a1b2c3d4-...",
      "job_post_id": "e5f6a7b8-...",
      "username": "johndoe",
      "family_name": "Doe",
      "given_name": "John",
      "email": "john@example.com",
      "phone": "+1234567890",
      "linkedin_url": "https://linkedin.com/in/johndoe",
      "portfolio_url": "https://johndoe.dev",
      "resume_url": "https://storage.googleapis.com/.../resume.pdf",
      "cover_letter": "I am excited to apply...",
      "additional_info": null,
      "job_title": "Senior Software Engineer",
      "status": "submitted",
      "created_at": "2026-01-15T10:30:00"
    }
  ],
  "total": 3,
  "page": 1,
  "limit": 20,
  "message": null
}
```

**Error Codes:**
| Code | Detail |
|------|--------|
| 401 | Not authenticated |
