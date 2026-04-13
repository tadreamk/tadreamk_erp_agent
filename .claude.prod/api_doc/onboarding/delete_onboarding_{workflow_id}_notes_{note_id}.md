# DELETE /onboarding/{workflow_id}/notes/{note_id}

Delete a note. Only the note author can delete.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| note_id | UUID | The note's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access. Talent is denied.

**Response:** `204 No Content`

**Errors:**
- `400` — Invalid workflow_id or note_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent / You can only modify your own notes
- `404` — Note not found
