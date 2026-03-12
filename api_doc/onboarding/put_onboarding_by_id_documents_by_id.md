# PUT /onboarding/{workflow_id}/documents/{document_id}


Update field values for a specific document. Accessible by HR, CEO, and Talent. Implements the **Signature Lock Rule**: once `talent_signature` exists, only fields prefixed with `ceo_` can be updated. Syncs field values to linked employee tables.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |
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
    "start_date": "2026-04-01",
    "salary": "5000"
  }
}
```

**Response:**
```json
{
  "message": "Document field values updated",
  "document": {
    "id": "uuid",
    "onboarding_id": "uuid",
    "template_id": "uuid",
    "document_type": "onboarding",
    "pdf_url": null,
    "field_values": { "full_name": "Jane Doe", "start_date": "2026-04-01", "salary": "5000" },
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": "2026-03-05T14:00:00+00:00",
    "template_name": "Employment Contract",
    "template_brief_description": "Standard employment agreement",
    "template_category": "contract",
    "fields": [],
    "is_locked": false
  }
}
```

**Errors:**
- `400` — Document is locked and update does not target CEO fields only
- `401` — Not authenticated
- `403` — No access to this onboarding workflow
- `404` — Onboarding workflow or document not found; document not in this workflow
