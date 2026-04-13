# GET /personal-notes/{note_id}

Get a single note by ID. Accessible by the note owner or any user the note is shared with. Requires authentication.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| note_id | UUID | Yes | The note ID |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "title": "string",
  "content": "markdown string or null",
  "category": "string",
  "shared_with": ["username1", "username2"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Access denied (not owner or shared recipient)
- `404` — Note not found
