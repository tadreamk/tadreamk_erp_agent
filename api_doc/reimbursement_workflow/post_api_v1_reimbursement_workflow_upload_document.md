# POST /api/v1/reimbursement-workflow/upload-document


Upload a supporting document to OneDrive and return the file URL. Use the returned URL in the `file_urls` field when creating or updating a reimbursement.

**Access control:** Authentication required (any user).

**Request:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | Document file to upload |

**Allowed file types:** `.pdf`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`

**Maximum file size:** 900 KB

**Response:**
```json
{
  "url": "https://onedrive.example.com/finance/reimbursement/john.doe_20260301_120000_receipt.pdf",
  "filename": "receipt.pdf",
  "size": 245760
}
```

**Errors:**
- `400` -- Invalid file type. Allowed: .pdf, .png, .jpg, .jpeg, .gif, .webp
- `400` -- File too large. Maximum size is 900KB.
- `401` -- Not authenticated
- `500` -- Failed to upload file: {error}
