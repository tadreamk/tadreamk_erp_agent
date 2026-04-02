# POST /onboarding/{workflow_id}/notes

Create a new internal note on an onboarding workflow. Sends notifications to mentioned users.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access. Talent is denied.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Note text (min 1 char) |
| mentioned_users | array[string] | No | Usernames to notify |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "username": "hr_user",
  "content": "Note text",
  "created_at": "2024-01-01T00:00:00+00:00",
  "updated_at": "2024-01-01T00:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent
- `404` — Workflow not found
