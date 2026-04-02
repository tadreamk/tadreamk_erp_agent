# POST /job-applications-workflow/{workflow_id}/interview-set-interviewers

Set interviewers for a workflow.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| interviewers | array[string] | Yes | List of interviewer usernames (min 1) |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Interviewers updated",
  "interviewers": ["alice", "bob"]
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Not on job-applications whitelist
- `404` — Workflow not found
