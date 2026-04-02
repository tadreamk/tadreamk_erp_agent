# PUT /onboarding/{workflow_id}/notes/{note_id}

Update a note. Only the note author can update.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| note_id | UUID | The note's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access. Talent is denied.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated note text (min 1 char) |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "username": "hr_user",
  "content": "Updated note text",
  "created_at": "2024-01-01T00:00:00+00:00",
  "updated_at": "2024-01-02T00:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid workflow_id or note_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent / You can only modify your own notes
- `404` — Note not found
