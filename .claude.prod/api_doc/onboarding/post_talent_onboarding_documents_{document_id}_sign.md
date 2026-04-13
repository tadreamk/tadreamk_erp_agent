# POST /talent/onboarding/documents/{document_id}/sign

Talent signs a document, locking it from further modification. Workflow must be in `talent_input` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | The document's unique identifier |

**Auth:** Requires authentication. Must be the talent on the workflow.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| talent_signature | string | Yes | Base64 encoded signature data |

**Response:** `200 OK`
```json
{
  "message": "Document signed and locked",
  "document": { "...OnboardingDocumentResponse..." }
}
```

**Errors:**
- `400` — Can only perform this action when status is talent_input
- `400` — Document is already signed
- `400` — Signature is required
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Document or workflow not found
