# POST /technical-reports/upload


Upload a supporting file to Google Cloud Storage. Returns the file URL for use in `file_urls` when creating a report.

**Request Body:** `multipart/form-data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | File to upload |

**Allowed file types:** `.pdf`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.doc`, `.docx`

**Maximum file size:** 900 KB

**Response:**
```json
{
  "url": "https://storage.googleapis.com/bucket/technical-reports/john.doe_20260310_090000_screenshot.png",
  "filename": "screenshot.png",
  "size": 45678
}
```

**Errors:**
- `400` — Invalid file type / File too large (max 900KB)
- `401` — Not authenticated
- `403` — Only employees can submit technical reports
- `500` — Failed to upload file to GCS
