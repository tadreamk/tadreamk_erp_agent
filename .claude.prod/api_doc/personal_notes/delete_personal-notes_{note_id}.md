# DELETE /personal-notes/{note_id}

Soft delete a personal note. Only the note owner can delete. Requires authentication.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| note_id | UUID | Yes | The note ID |

**Response:** `204 No Content`

**Errors:**
- `401` — Not authenticated
- `403` — Only the note owner can delete
- `404` — Note not found
