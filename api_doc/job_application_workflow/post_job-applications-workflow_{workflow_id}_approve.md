# POST /job-applications-workflow/{workflow_id}/approve

Approve a candidate for a specific position. Creates onboarding workflow automatically. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| job_post_id | UUID | Yes | The job post ID to approve for |

**Response:**
```json
{
  "success": true,
  "message": "Candidate approved",
  "new_status": "approved",
  "final_decision_by": "alice",
  "final_decision_at": "datetime"
}
```

**Errors:**
- `400` — job_post_id does not match any application in this workflow, or workflow not in decidable state
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
