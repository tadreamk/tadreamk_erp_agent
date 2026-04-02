# GET /job-applications-workflow/{workflow_id}/exercise-content

Get exercise content for a workflow. Accessible by staff (whitelist) or the candidate.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist or workflow owner access.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "title": "Backend API Exercise",
  "tags": ["backend", "database"],
  "content": "Exercise description markdown..."
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Access denied
- `404` — Workflow not found / No exercise assigned / Exercise not found
