# POST /job-applications-workflow/{workflow_id}/interview-set-interviewers


Set or update the list of interviewers for a workflow.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| interviewers | string[] | Yes | List of interviewer usernames (at least 1) |

**Request Example:**
```json
{
  "interviewers": ["tech_lead", "engineering_manager"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Interviewers updated",
  "interviewers": ["tech_lead", "engineering_manager"]
}
```

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
- `422` — Validation error (empty interviewers list)
