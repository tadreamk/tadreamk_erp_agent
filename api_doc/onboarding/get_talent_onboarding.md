# GET /talent/onboarding


Get the authenticated talent's onboarding workflows. Returns all active (non-cancelled) workflows, with the first one as the primary workflow.

**Response (workflows found):**
```json
{
  "workflow": {
    "id": "uuid",
    "talent_email": "jane.doe@example.com",
    "talent_username": "jane.doe",
    "hr_username": "hr.admin",
    "ceo_username": "ceo.user",
    "status": "input",
    "talent_submitted_at": null,
    "sent_to_ceo_at": null,
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": null,
    "is_active": true,
    "documents": [
      {
        "id": "uuid",
        "onboarding_id": "uuid",
        "template_id": "uuid",
        "document_type": "onboarding",
        "pdf_url": null,
        "field_values": {},
        "created_at": "2026-03-01T10:00:00+00:00",
        "updated_at": null,
        "template_name": "Employment Contract",
        "template_brief_description": "Standard employment agreement",
        "template_category": "contract",
        "fields": [],
        "is_locked": false
      }
    ]
  },
  "workflows": [ "..." ]
}
```

**Response (no workflows):**
```json
{
  "message": "No onboarding found",
  "workflow": null,
  "workflows": []
}
```

**Errors:**
- `401` — Not authenticated
