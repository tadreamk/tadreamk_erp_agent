# GET /job-applications-workflow/{workflow_id}/notes


List all notes for a workflow.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Response:**
```json
{
  "notes": [
    {
      "id": "uuid-string",
      "workflow_id": "uuid-string",
      "username": "staff_user",
      "content": "Candidate has strong backend experience.",
      "created_at": "2026-01-15T10:30:00+00:00",
      "updated_at": "2026-01-15T10:30:00+00:00"
    }
  ],
  "total": 1
}
```

**Errors:**
- `400` — Invalid workflow_id UUID format
- `401` — Not authenticated
- `403` — Staff access required
- `404` — Workflow not found
