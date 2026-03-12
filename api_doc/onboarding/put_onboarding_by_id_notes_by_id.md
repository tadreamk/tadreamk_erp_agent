# PUT /onboarding/{workflow_id}/notes/{note_id}


Update a note. Only the original author can update.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string (UUID) | Onboarding workflow ID |
| note_id | string (UUID) | Note ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No | Updated note text (min 1 character) |

**Request Example:**
```json
{
  "content": "Updated: Salary confirmed at 5000/month."
}
```

**Response:**
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "username": "hr.admin",
  "content": "Updated: Salary confirmed at 5000/month.",
  "created_at": "2026-03-05T09:00:00+00:00",
  "updated_at": "2026-03-05T10:30:00+00:00"
}
```

**Errors:**
- `400` — Invalid workflow_id or note_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent; you can only modify your own notes; no access to workflow
- `404` — Note not found
