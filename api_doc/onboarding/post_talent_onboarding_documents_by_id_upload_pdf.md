# POST /talent/onboarding/documents/{document_id}/upload-pdf


Talent uploads a PDF file for a document to OneDrive. Workflow must be in `input` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | UUID | Document ID |

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file (PDF) | Yes | The PDF file to upload |

**Response:**
```json
{
  "message": "PDF uploaded successfully",
  "pdf_url": "https://onedrive.example.com/path/to/file.pdf"
}
```

**Errors:**
- `400` — Workflow not in `input` status
- `401` — Not authenticated
- `403` — Not authorized (email mismatch)
- `404` — Document or workflow not found
