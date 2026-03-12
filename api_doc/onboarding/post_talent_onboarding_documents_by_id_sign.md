# POST /talent/onboarding/documents/{document_id}/sign


Talent signs a document. This locks the document, preventing further field edits by the talent. Signature is synced to the employee contract table.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | Document ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| talent_signature | string | Yes | Signature data (base64 encoded image) |

**Request Example:**
```json
{
  "talent_signature": "data:image/png;base64,iVBORw0KGgo..."
}
```

**Response:**
```json
{
  "message": "Document signed and locked",
  "document": {
    "id": "uuid",
    "onboarding_id": "uuid",
    "template_id": "uuid",
    "document_type": "onboarding",
    "pdf_url": null,
    "field_values": { "full_name": "Jane Doe", "talent_signature": "data:image/png;base64,..." },
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": "2026-03-06T12:00:00+00:00",
    "template_name": "Employment Contract",
    "template_brief_description": "Standard employment agreement",
    "template_category": "contract",
    "fields": [],
    "is_locked": true
  }
}
```

**Errors:**
- `400` — Document is already signed; signature is required; workflow not in `input` status
- `401` — Not authenticated
- `403` — Not authorized (email mismatch)
- `404` — Document or workflow not found
