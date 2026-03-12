# POST /onboarding/{workflow_id}/notes


Create a new note on a workflow. Optionally mention other users to trigger notifications.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string (UUID) | Onboarding workflow ID |

**Access:** HR or CEO only.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Note text (min 1 character) |
| mentioned_users | array of strings | No | Usernames to notify via mention |

**Request Example:**
```json
{
  "content": "Please review the salary figure @ceo.user",
  "mentioned_users": ["ceo.user"]
}
```

**Response (201):**
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "username": "hr.admin",
  "content": "Please review the salary figure @ceo.user",
  "created_at": "2026-03-05T09:00:00+00:00",
  "updated_at": "2026-03-05T09:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent; no access to workflow
- `404` — Onboarding workflow not found
