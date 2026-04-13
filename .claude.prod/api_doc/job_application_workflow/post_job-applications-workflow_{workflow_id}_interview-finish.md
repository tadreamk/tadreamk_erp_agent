# POST /job-applications-workflow/{workflow_id}/interview-finish

Mark interview as finished.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist access.

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Interview finished",
  "status": "interview_done"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Not on job-applications whitelist
- `404` — Workflow not found
