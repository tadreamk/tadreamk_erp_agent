# GET /templates/{template_id}/onboarding/{document_id}


Get template with field values populated from an onboarding document. Access is granted to HR (via whitelist), the onboarding talent, or the CEO assigned to the workflow.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| template_id | string (UUID) | Yes | Template unique identifier |
| document_id | string (UUID) | Yes | Onboarding document unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "title": "Employment Contract",
  "description": "Standard employment contract template",
  "category": "onboarding",
  "fields": [],
  "pdf_url": null,
  "is_active": true,
  "version": 1,
  "created_at": "2026-01-10T08:00:00+00:00",
  "updated_at": "2026-01-10T08:00:00+00:00",
  "field_values": {
    "employee_name": "John Doe",
    "start_date": "2026-03-01"
  },
  "onboarding_document_id": "uuid",
  "onboarding_id": "uuid",
  "user_role": "hr"
}
```

**`user_role` values:** `hr`, `talent`, `ceo`

**Errors:**
- `400` — Invalid document ID format / Template ID mismatch
- `401` — Not authenticated
- `403` — No access to this document
- `404` — Onboarding document or workflow not found
