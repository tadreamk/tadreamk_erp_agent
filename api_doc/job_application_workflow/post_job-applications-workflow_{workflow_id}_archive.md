# POST /job-applications-workflow/{workflow_id}/archive

Archive a workflow. No notification sent. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Archive reason |

**Response:**
```json
{
  "success": true,
  "message": "Workflow archived",
  "new_status": "archived",
  "final_decision_by": "alice",
  "final_decision_at": "datetime"
}
```

**Errors:**
- `400` — Workflow not in decidable state
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
