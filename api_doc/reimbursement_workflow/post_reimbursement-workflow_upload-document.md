# POST /reimbursement-workflow/upload-document

Upload a supporting document to OneDrive and return the file URL. Requires authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | Document file to upload |

**Response:**
```json
{
  "url": "https://onedrive.example.com/files/document.pdf"
}
```

**Errors:**
- `401` — Not authenticated
- `400` — File upload failed
