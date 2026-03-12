# PATCH /job-applications-workflow/{workflow_id}/bookmark


Toggle the bookmark flag on a workflow.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Response:**
```json
{
  "bookmark": true,
  "workflow_id": "uuid-string"
}
```

**Errors:**
- `400` — Invalid workflow_id UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found

---

## 13. Job Application Workflow (Actions)

Final decision endpoints for approving, rejecting, or archiving a candidate. These actions can be taken from any "decidable" status: `submitted`, `exercise_assigned`, `exercise_submitted`, `exercise_scored`, `interview_proposed`, `interview_negotiating`, `interview_confirmed`, `interview_finished`.
