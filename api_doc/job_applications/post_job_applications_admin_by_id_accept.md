# POST /job-applications/admin/{application_id}/accept


Accept a candidate. Changes status to `accepted`, sends an acceptance email, creates an onboarding workflow with documents from onboarding templates, and notifies the head of HR.

**Precondition:** Application must be in `interview_confirmed` or `interview_finished` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| template_id | string (UUID) | No | Contract template ID (uses default if not provided) |
| proposed_start_date | string | No | Proposed start date (format: `YYYY-MM-DD`) |
| salary | string | No | Salary amount |
| notes | string | No | Additional notes for the contract |

**Example Request:**
```json
{
  "proposed_start_date": "2026-04-01",
  "salary": "85000",
  "notes": "Remote position, probation 3 months"
}
```

**Response (200):**
```json
{
  "message": "Candidate accepted successfully",
  "application": {
    "id": "a1b2c3d4-...",
    "status": "accepted",
    "...": "..."
  },
  "onboarding_workflow_id": "f1e2d3c4-..."
}
```

The `onboarding_workflow_id` field is only present if the onboarding workflow was created successfully.

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format, or application is not in `interview_confirmed` / `interview_finished` status |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |
