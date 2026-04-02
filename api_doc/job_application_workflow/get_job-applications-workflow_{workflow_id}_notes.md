# GET /job-applications-workflow/{workflow_id}/notes

List internal staff notes for a workflow. Notes are not visible to talent/candidates. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Response:**
```json
{
  "notes": [
    {
      "id": "uuid",
      "workflow_id": "uuid",
      "content": "Note content...",
      "username": "bob",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
