# DELETE /personal-notes/{note_id}/shares/{username}

Remove sharing access for a specific user. Only the note owner can manage shares. Requires authentication.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| note_id | UUID | Yes | The note ID |
| username | string | Yes | The username to remove sharing access for |

**Response:** `204 No Content`

**Errors:**
- `401` — Not authenticated
- `403` — Only the note owner can manage shares
- `404` — Note not found, or share not found
