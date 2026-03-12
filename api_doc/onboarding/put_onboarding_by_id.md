# PUT /onboarding/{workflow_id}


Update an onboarding workflow (HR only). Status transitions are validated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | No | New workflow status (must be a valid transition) |
| hr_username | string | No | Reassign HR user |
| ceo_username | string | No | Reassign CEO user |

**Request Example:**
```json
{
  "status": "pending_ceo_confirmation",
  "hr_username": "hr.new"
}
```

**Response:**
```json
{
  "message": "Onboarding workflow updated",
  "workflow": {
    "id": "uuid",
    "talent_email": "jane.doe@example.com",
    "talent_username": "jane.doe",
    "hr_username": "hr.new",
    "ceo_username": "ceo.user",
    "status": "pending_ceo_confirmation",
    "talent_submitted_at": null,
    "sent_to_ceo_at": null,
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": "2026-03-05T14:00:00+00:00",
    "is_active": true,
    "document_count": 3
  }
}
```

**Errors:**
- `400` — Invalid status value or invalid status transition
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
