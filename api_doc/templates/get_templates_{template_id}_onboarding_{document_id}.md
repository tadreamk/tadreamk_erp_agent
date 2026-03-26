# GET /templates/{template_id}/onboarding/{document_id}

Get a template with field values pre-filled from an onboarding document. User must have access to the onboarding workflow (HR, talent, or CEO). Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | UUID | The template's unique identifier |
| document_id | UUID | The onboarding document's unique identifier |

**Response:** Template object with additional fields
```json
{
  "id": "uuid",
  "name": "string",
  "field_values": {},
  "onboarding_document_id": "uuid",
  "onboarding_id": "uuid",
  "user_role": "hr"
}
```

**Errors:**
- `400` — Invalid template or document ID format; or template ID mismatch
- `401` — Not authenticated
- `403` — No access to this onboarding document
- `404` — Template or onboarding document not found
