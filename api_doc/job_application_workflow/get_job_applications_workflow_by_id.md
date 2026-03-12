# GET /job-applications-workflow/{workflow_id}


Get full workflow detail including applicant info, applied positions, exercise fields, interview fields, and decision fields.

**Access:** Whitelist (`job-applications`) **or** the candidate who owns the workflow.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Response:**
```json
{
  "id": "uuid-string",
  "username": "candidate1",
  "status": "exercise_scored",
  "bookmark": false,
  "created_at": "2026-01-01T08:00:00+00:00",
  "updated_at": "2026-01-15T10:30:00+00:00",

  "candidate_name": "John Doe",
  "email": "john@example.com",
  "phone": "+66812345678",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "portfolio_url": "https://johndoe.dev",
  "resume_url": "https://storage.example.com/resumes/johndoe.pdf",
  "cover_letter": "I am excited to apply...",
  "additional_info": null,
  "family_name": "Doe",
  "given_name": "John",

  "applications": [
    {
      "job_application_id": "uuid-string",
      "job_post_id": "uuid-string",
      "job_title": "Backend Engineer",
      "applied_at": "2026-01-01T08:00:00+00:00"
    }
  ],

  "exercise_id": "uuid-string",
  "exercise_github_url": "https://github.com/johndoe/exercise",
  "exercise_report_url": "https://docs.google.com/document/d/abc",
  "exercise_score": 4,
  "exercise_scored_by": "tech_lead",
  "exercise_scored_at": "2026-01-10T14:00:00+00:00",

  "interview_schedule_admin": ["2026-01-20 10:00", "2026-01-21 14:00"],
  "interview_schedule_final": "2026-01-20 10:00",
  "interview_url": "https://meet.google.com/abc-defg-hij",
  "interview_score": 4,
  "interview_scored_by": "tech_lead",
  "interview_scored_at": "2026-01-20T11:00:00+00:00",
  "interviewers": ["tech_lead", "engineering_manager"],

  "accepted_job_post_id": null,
  "final_decision_by": null,
  "final_decision_at": null,
  "rejection_reason": null
}
```

**Errors:**
- `400` — Invalid workflow_id UUID format
- `401` — Not authenticated
- `403` — Access denied (not staff and not workflow owner)
- `404` — Workflow not found
