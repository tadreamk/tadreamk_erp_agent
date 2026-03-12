# GET /onboarding/{workflow_id}/documents


List all documents for a workflow with template details (HR only).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
[
  {
    "id": "uuid",
    "onboarding_id": "uuid",
    "template_id": "uuid",
    "document_type": "onboarding",
    "pdf_url": null,
    "field_values": { "full_name": "Jane Doe" },
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": null,
    "template_name": "Employment Contract",
    "template_brief_description": "Standard employment agreement",
    "template_category": "contract",
    "fields": [
      { "field_name": "full_name", "field_key": "full_name", "data_type": "text", "input_by_role": "employee" }
    ],
    "is_locked": false
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
