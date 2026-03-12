# POST /job-applications-workflow/{workflow_id}/archive


Archive a workflow. No notifications are sent.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Optional archive reason |

**Request Example:**
```json
{
  "reason": "Candidate withdrew their application."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Workflow archived",
  "new_status": "archived",
  "final_decision_by": "hr_manager",
  "final_decision_at": "2026-01-25T09:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid UUID format / workflow not in a decidable status
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found

---

## 14. Job Application Workflow (Exercise)

Exercise assignment, submission, scoring, and content retrieval (Steps 2-4 of the workflow).
