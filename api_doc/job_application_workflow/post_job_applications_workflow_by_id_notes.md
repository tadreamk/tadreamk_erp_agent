# POST /job-applications-workflow/{workflow_id}/notes


Create a new note on a workflow. Optionally mention other staff users (triggers in-app notifications).

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Note text content (min length: 1) |
| mentioned_users | string[] | No | List of staff usernames to mention/notify |

**Request Example:**
```json
{
  "content": "Reviewed the candidate's portfolio - impressive work on data pipelines.",
  "mentioned_users": ["recruiter1", "tech_lead"]
}
```

**Response (201 Created):**
```json
{
  "id": "uuid-string",
  "workflow_id": "uuid-string",
  "username": "staff_user",
  "content": "Reviewed the candidate's portfolio - impressive work on data pipelines.",
  "created_at": "2026-01-15T10:30:00+00:00",
  "updated_at": "2026-01-15T10:30:00+00:00"
}
```

**Errors:**
- `400` — Invalid workflow_id UUID format
- `401` — Not authenticated
- `403` — Staff access required
- `404` — Workflow not found
- `422` — Validation error (empty content)
