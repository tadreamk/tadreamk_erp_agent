# POST /onboarding/{workflow_id}/documents/{document_id}/upload-pdf

Upload a PDF or image file to OneDrive for an onboarding document (HR upload).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| document_id | UUID | The document's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

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
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow or document not found
- `500` — Failed to upload to OneDrive
