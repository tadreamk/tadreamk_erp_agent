# POST /job-applications/submit


Submit a new job application with resume file upload. Sends a confirmation email to the candidate and an in-app notification to the head of recruitment.

**Content-Type:** `multipart/form-data`

**Request Body (form fields):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| job_post_id | string (UUID) | Yes | ID of the job post being applied to |
| email | string (email) | Yes | Applicant's email address |
| phone | string | Yes | Applicant's phone number (max 50 chars) |
| cover_letter | string | Yes | Cover letter text |
| family_name | string | No | Applicant's family name (max 100 chars) |
| given_name | string | No | Applicant's given name (max 100 chars) |
| linkedin_url | string | No | LinkedIn profile URL |
| portfolio_url | string | No | Portfolio or personal website URL |
| additional_info | string | No | Any additional information |
| resume | file (UploadFile) | Yes | Resume file upload |

**Response (200):**
```json
{
  "message": "Application submitted successfully",
  "success": true,
  "data": {
    "id": "a1b2c3d4-...",
    "status": "submitted"
  }
}
```

**Error Codes:**
| Code | Detail |
|------|--------|
| 401 | Not authenticated |
| 409 | Duplicate application (user already applied to this job post) |
| 400 | Invalid resume file or validation error |
