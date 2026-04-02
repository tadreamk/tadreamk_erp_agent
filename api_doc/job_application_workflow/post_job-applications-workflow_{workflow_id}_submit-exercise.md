# POST /job-applications-workflow/{workflow_id}/submit-exercise

Submit exercise URLs. Talent only — must be the workflow owner.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires authentication. Must be the candidate on the workflow.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| github_url | string | No | GitHub repository URL |
| report_url | string | No | Report document URL |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Exercise submitted successfully",
  "status": "exercise_submitted"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — You can only submit exercises for your own application
- `404` — Workflow not found
