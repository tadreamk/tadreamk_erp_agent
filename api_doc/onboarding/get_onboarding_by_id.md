# GET /onboarding/{workflow_id}


Get a single onboarding workflow with all documents and template details. Accessible by HR, Talent, and CEO.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "id": "uuid",
  "talent_email": "talent@example.com",
  "talent_username": "jane.doe",
  "hr_username": "hr.admin",
  "ceo_username": "ceo.user",
  "status": "input",
  "talent_submitted_at": "2026-03-10T08:00:00+00:00",
  "sent_to_ceo_at": null,
  "created_at": "2026-03-01T10:00:00+00:00",
  "updated_at": "2026-03-10T08:00:00+00:00",
  "is_active": true,
  "documents": [
    {
      "id": "uuid",
      "onboarding_id": "uuid",
      "template_id": "uuid",
      "document_type": "onboarding",
      "pdf_url": null,
      "field_values": { "full_name": "Jane Doe", "talent_signature": null },
      "created_at": "2026-03-01T10:00:00+00:00",
      "updated_at": null,
      "template_name": "Employment Contract",
      "template_brief_description": "Standard employment agreement",
      "template_category": "contract",
      "fields": [
        { "field_name": "full_name", "field_key": "full_name", "data_type": "text", "input_by_role": "employee" },
        { "field_name": "ceo_signature", "field_key": "ceo_signature", "data_type": "signature", "input_by_role": "ceo" }
      ],
      "is_locked": false
    }
  ],
  "user_role": "hr"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this onboarding workflow
- `404` — Onboarding workflow not found
