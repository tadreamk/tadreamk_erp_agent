# POST /talent/onboarding/documents/{document_id}/upload-pdf

Talent uploads a PDF or image file to OneDrive for an onboarding document. Workflow must be in `talent_input` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | The document's unique identifier |

**Auth:** Requires authentication. Must be the talent on the workflow.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | PDF or image file (.pdf, .jpg, .jpeg, .png, .webp). Max 4MB. |

**Response:** `200 OK`
```json
{
  "message": "File uploaded successfully",
  "onedrive_url": "https://...",
  "filename": "workflow_id_template_id.pdf",
  "document": { "...OnboardingDocumentResponse..." }
}
```

**Errors:**
- `400` — Document is locked after signing
- `400` — Only PDF and image files are allowed
- `400` — File too large (max 4MB)
- `400` — Can only perform this action when status is talent_input
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Document or workflow not found
- `500` — Failed to upload to OneDrive
