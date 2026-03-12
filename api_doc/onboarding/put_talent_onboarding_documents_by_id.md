# PUT /talent/onboarding/documents/{document_id}


Talent updates their field values on a document. Document must not be locked (signed). Workflow must be in `input` status. Field values are synced to linked employee tables.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | Document ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Key-value pairs of fields to update/merge |

**Request Example:**
```json
{
  "field_values": {
    "full_name": "Jane Doe",
    "address": "123 Main St",
    "phone": "+65 9123 4567"
  }
}
```

**Response:**
```json
{
  "message": "Document updated",
  "document": {
    "id": "uuid",
    "onboarding_id": "uuid",
    "template_id": "uuid",
    "document_type": "onboarding",
    "pdf_url": null,
    "field_values": { "full_name": "Jane Doe", "address": "123 Main St", "phone": "+65 9123 4567" },
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": "2026-03-06T11:00:00+00:00",
    "template_name": "Employment Contract",
    "template_brief_description": "Standard employment agreement",
    "template_category": "contract",
    "fields": [],
    "is_locked": false
  }
}
```

**Errors:**
- `400` — Document is locked after signing; workflow not in `input` status
- `401` — Not authenticated
- `403` — Not authorized (email mismatch)
- `404` — Document or workflow not found
