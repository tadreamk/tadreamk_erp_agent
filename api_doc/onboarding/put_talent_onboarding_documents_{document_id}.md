# PUT /talent/onboarding/documents/{document_id}

Talent updates their fields on a document. Workflow must be in `talent_input` status. Document must not be locked (signed).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | The document's unique identifier |

**Auth:** Requires authentication. Must be the talent on the workflow.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Field values to update/merge |

**Response:** `200 OK`
```json
{
  "message": "Document updated",
  "document": { "...OnboardingDocumentResponse..." }
}
```

**Errors:**
- `400` — Can only perform this action when status is talent_input
- `400` — Document is locked after signing
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Document or workflow not found
