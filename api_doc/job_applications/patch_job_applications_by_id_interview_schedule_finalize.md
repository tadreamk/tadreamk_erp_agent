# PATCH /job-applications/{application_id}/interview-schedule-finalize


Finalize the interview schedule by selecting a confirmed time. Sets the `interview_schedule_final` field, clears proposals, sets status to `interview_confirmed`, and sends a confirmation email to the candidate with a static Microsoft Teams meeting URL.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| selected_time | string | Yes | Confirmed interview time in ISO 8601 UTC format. Example: `"2026-04-10T14:00:00Z"` |

**Example Request:**
```json
{
  "selected_time": "2026-04-10T14:00:00Z"
}
```

**Response (200):** Updated `JobApplicationResponse` object (status will be `interview_confirmed`).

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format or invalid datetime format |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |
| 500 | Failed to finalize interview schedule |

---

## Common Response Schema: JobApplicationResponse

All endpoints that return application data use this schema:

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| id | string (UUID) | No | Application ID |
| job_post_id | string (UUID) | No | Job post ID |
| username | string | No | Applicant's username |
| family_name | string | Yes | Applicant's family name |
| given_name | string | Yes | Applicant's given name |
| email | string | No | Applicant's email address |
| phone | string | No | Applicant's phone number |
| linkedin_url | string | Yes | LinkedIn profile URL |
| portfolio_url | string | Yes | Portfolio URL |
| resume_url | string | No | Public URL to the uploaded resume file |
| cover_letter | string | No | Cover letter text |
| additional_info | string | Yes | Additional information |
| job_title | string | Yes | Job title (resolved from the linked job post) |
| status | string | Yes | Current workflow status (from `ApplicationStatus` enum) |
| created_at | datetime | No | Application submission timestamp |
