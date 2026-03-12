# PUT /job-applications-workflow/{workflow_id}/notes/{note_id}


Update a note. Only the original author can update.

**Access:** Whitelist (`job-applications`) + note author only

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |
| note_id | UUID | Yes | Note ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated note text content (min length: 1) |

**Request Example:**
```json
{
  "content": "Updated assessment: strong candidate, recommend proceeding to interview."
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "workflow_id": "uuid-string",
  "username": "staff_user",
  "content": "Updated assessment: strong candidate, recommend proceeding to interview.",
  "created_at": "2026-01-15T10:30:00+00:00",
  "updated_at": "2026-01-15T11:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Staff access required / not the note author
- `404` — Note not found
- `422` — Validation error
