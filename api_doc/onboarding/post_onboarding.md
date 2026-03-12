# POST /onboarding


Create a new onboarding workflow (HR only).

**Request Body:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| talent_email | string (email) | Yes | — | New hire's email address |
| talent_username | string | Yes | — | New hire's username |
| hr_username | string | Yes | — | Assigned HR username |
| ceo_username | string | Yes | — | Assigned CEO username |
| status | string | No | `"draft"` | Initial workflow status |

**Request Example:**
```json
{
  "talent_email": "jane.doe@example.com",
  "talent_username": "jane.doe",
  "hr_username": "hr.admin",
  "ceo_username": "ceo.user",
  "status": "template_selection"
}
```

**Response (201):**
```json
{
  "message": "Onboarding workflow created",
  "workflow": {
    "id": "uuid",
    "talent_email": "jane.doe@example.com",
    "talent_username": "jane.doe",
    "hr_username": "hr.admin",
    "ceo_username": "ceo.user",
    "status": "template_selection",
    "talent_submitted_at": null,
    "sent_to_ceo_at": null,
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": null,
    "is_active": true,
    "document_count": 0
  }
}
```

**Errors:**
- `400` — Invalid status value
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
