# POST /job-applications-workflow/{workflow_id}/interview-finish


Mark an interview as finished.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Response:**
```json
{
  "success": true,
  "message": "Interview finished",
  "new_status": "interview_finished"
}
```

**Side Effects:**
- Sets status to `interview_finished`

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
