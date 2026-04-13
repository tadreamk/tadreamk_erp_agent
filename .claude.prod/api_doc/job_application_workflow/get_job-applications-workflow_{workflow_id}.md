# GET /job-applications-workflow/{workflow_id}

Get full workflow detail including applicant info and positions. Accessible by staff (whitelist) or the candidate who owns the workflow.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Response:** Full workflow detail object with applicant info and job applications

**Errors:**
- `401` — Not authenticated
- `403` — Access denied (not staff and not workflow owner)
- `404` — Workflow not found
