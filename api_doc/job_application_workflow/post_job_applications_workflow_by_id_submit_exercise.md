# POST /job-applications-workflow/{workflow_id}/submit-exercise


Submit exercise solution URLs. Only the candidate who owns the workflow can submit.

**Access:** Authenticated (workflow owner only)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| github_url | string | No | GitHub repository URL |
| report_url | string | No | Report/document URL |

**Request Example:**
```json
{
  "github_url": "https://github.com/candidate/exercise-repo",
  "report_url": "https://docs.google.com/document/d/abc123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Exercise submitted successfully",
  "new_status": "exercise_submitted"
}
```

**Side Effects:**
- Sets status to `exercise_submitted`
- Sends in-app notification to users with the `head_of_it` role

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Not the workflow owner
- `404` — Workflow not found
