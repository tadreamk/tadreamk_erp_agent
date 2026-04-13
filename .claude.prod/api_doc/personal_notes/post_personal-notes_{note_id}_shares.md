# POST /personal-notes/{note_id}/shares

Share a note with one or more employees. Only the note owner can share. Sends a notification to each recipient. Requires authentication.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| note_id | UUID | Yes | The note ID |

**Request Body:**
```json
{
  "usernames": ["username1", "username2"]
}
```

The `usernames` array must contain at least one username. Cannot share with yourself.

**Response (201):**
```json
{
  "shared_with": ["username1", "username2"]
}
```

**Errors:**
- `400` — Cannot share with yourself
- `401` — Not authenticated
- `403` — Only the note owner can share
- `404` — Note not found
