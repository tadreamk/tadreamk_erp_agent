# POST /reimbursement-workflow/upload-document

Upload a supporting document to OneDrive and return the file URL. Requires authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | Document file to upload |

**Response:**
```json
{
  "url": "https://onedrive.example.com/files/document.pdf",
  "filename": "document.pdf",
  "size": 102400
}
```

**Errors:**
- `401` — Not authenticated
- `400` — File upload failed
