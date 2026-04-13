# GET /onboarding/{workflow_id}/documents

List all documents for a workflow with template details.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK` — Array of `OnboardingDocumentResponse`
```json
[
  {
    "id": "uuid",
    "onboarding_id": "uuid",
    "template_id": "uuid",
    "document_type": "onboarding",
    "pdf_url": null,
    "field_values": {},
    "created_at": "2024-01-01T00:00:00",
    "updated_at": null,
    "template_name": "Employment Contract",
    "template_brief_description": "Standard employment contract",
    "template_category": "contracts",
    "fields": [],
    "is_locked": false
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
