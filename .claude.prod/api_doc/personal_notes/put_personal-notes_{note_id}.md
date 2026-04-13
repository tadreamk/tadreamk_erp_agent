# PUT /personal-notes/{note_id}

Update a personal note. Only the note owner can edit. Requires authentication.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| note_id | UUID | Yes | The note ID |

**Request Body:**
```json
{
  "title": "string (optional, 1-500 chars)",
  "content": "markdown string (optional)",
  "category": "string (optional)"
}
```

All fields are optional — only provided fields are updated.

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "title": "string",
  "content": "markdown string or null",
  "category": "string",
  "shared_with": ["username1"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only the note owner can edit
- `404` — Note not found
- `422` — Validation error
