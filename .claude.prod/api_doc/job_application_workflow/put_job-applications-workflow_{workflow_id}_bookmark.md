# PUT /job-applications-workflow/{workflow_id}/bookmark

Toggle the bookmark flag on a workflow. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Response:**
```json
{
  "bookmark": true,
  "workflow_id": "uuid"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
