# DELETE /job-applications-workflow/{workflow_id}/notes/{note_id}

Delete a workflow note. Only the note author can delete. Returns 204 No Content. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| note_id | UUID | The note's unique identifier |

**Response:** `204 No Content`

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access or not the note author
- `404` — Note not found
