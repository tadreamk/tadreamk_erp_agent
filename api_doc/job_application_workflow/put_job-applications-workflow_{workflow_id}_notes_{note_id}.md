# PUT /job-applications-workflow/{workflow_id}/notes/{note_id}

Update a workflow note. Only the note author can update. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| note_id | UUID | The note's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated note content |
| mentioned_users | list[string] | No | Updated mentioned users |

**Response:** Updated note object

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access or not the note author
- `404` — Note not found
