# PUT /onboarding/{workflow_id}/documents/{document_id}

Update field values for a document. Implements Signature Lock Rule: if a talent signature exists, only CEO fields (`ceo_*`) can be updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| document_id | UUID | The document's unique identifier |

**Auth:** Requires `onboarding` whitelist or owner access (HR or CEO).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Field values to update/merge |

**Response:** `200 OK`
```json
{
  "message": "Document field values updated",
  "document": { "...OnboardingDocumentResponse..." }
}
```

**Errors:**
- `400` — Document is locked, only CEO fields can be updated
- `401` — Not authenticated
- `403` — No access to this workflow
- `404` — Workflow or document not found
