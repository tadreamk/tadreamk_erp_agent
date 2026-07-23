# POST /job-application/submit

Submit Application. Requires authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| job_post_id | string | Yes |  |
| email | string | Yes |  |
| phone | string | Yes |  |
| cover_letter | string | Yes |  |
| family_name | string | No |  |
| given_name | string | No |  |
| linkedin_url | string | No |  |
| portfolio_url | string | No |  |
| additional_info | string | No |  |
| resume | string | Yes |  |

**Response:**
```json
{
  "application": {
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
  },
  "workflow": {
    "id": "uuid",
    "username": "string",
    "username_preferred_name": "string",
    "candidate_display_name": "string",
    "status": "string",
    "bookmark": false,
    "job_application_ids": [
      "uuid"
    ],
    "linked_applications": [
      {
        "id": "uuid",
        "job_post_id": "uuid",
        "job_post_title": {},
        "username": "string",
        "username_preferred_name": {},
        "family_name": {},
        "given_name": {},
        "email": "string",
        "phone": "string",
        "linkedin_url": {},
        "portfolio_url": {},
        "resume_url": "string",
        "cover_letter": "string",
        "additional_info": {},
        "created_at": "datetime"
      }
    ],
    "exercise_id": "uuid",
    "assigned_exercise": {
      "id": "uuid",
      "title": "string",
      "content": {},
      "status": {}
    },
    "exercise_github_url": "string",
    "exercise_report_url": "string",
    "exercise_score": 0,
    "exercise_scored_by": "string",
    "exercise_scored_by_preferred_name": "string",
    "exercise_scored_at": "datetime",
    "interview_slots_proposed": [
      "string"
    ],
    "interview_slot_final": "string",
    "interview_url": "string",
    "interview_score": 0,
    "interview_scored_by": "string",
    "interview_scored_by_preferred_name": "string",
    "interview_scored_at": "datetime",
    "interviewers": [
      {}
    ],
    "accepted_job_post_id": "uuid",
    "accepted_job_post_title": "string",
    "final_decision_by": "string",
    "final_decision_by_preferred_name": "string",
    "final_decision_at": "datetime",
    "rejection_reason": "string",
    "notes": [
      {
        "id": "uuid",
        "workflow_id": "uuid",
        "author_username": "string",
        "author_preferred_name": {},
        "content": "string",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    ],
    "created_at": "datetime",
    "updated_at": "datetime"
  },
  "is_new_workflow": false
}
```

**Errors:**
- `422` — Validation Error
