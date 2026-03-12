# POST /onboarding/{workflow_id}/documents/{document_id}/upload-pdf


Upload a PDF file for a document to OneDrive (HR). Used for documents that require a manual PDF upload instead of template-based field filling.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |
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
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow or document not found; document not in this workflow

---

## 28. Onboarding CEO Actions

Workflow actions performed by the CEO (or HR for `send-to-ceo`). CEO actions require the requesting user to be the assigned CEO for the workflow.
