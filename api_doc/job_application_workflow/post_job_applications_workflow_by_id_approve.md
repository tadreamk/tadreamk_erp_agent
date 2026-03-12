# POST /job-applications-workflow/{workflow_id}/approve


Approve a candidate for a specific position. Creates an onboarding workflow with documents and notifies `head_of_hr`.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| job_post_id | string (UUID) | Yes | Job post ID to accept the candidate for (must match one of the workflow's applications) |
| reason | string | No | Optional reason for approval |

**Request Example:**
```json
{
  "job_post_id": "uuid-of-job-post",
  "reason": "Excellent performance in exercise and interview."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Candidate approved",
  "new_status": "accepted",
  "final_decision_by": "hr_manager",
  "final_decision_at": "2026-01-25T09:00:00+00:00",
  "onboarding_workflow_id": "uuid-string"
}
```

**Side Effects:**
- Sets status to `accepted`
- Creates an onboarding workflow with associated onboarding documents
- Sends in-app notification to users with the `head_of_hr` role

**Errors:**
- `400` — Invalid UUID format / workflow not in a decidable status / job_post_id does not match any application in the workflow
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
