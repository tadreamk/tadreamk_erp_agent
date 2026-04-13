# POST /technical-reports/upload

Upload a supporting file to Google Cloud Storage and return the file URL. Requires employee authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | File to upload |

**Response:**
```json
{
  "url": "https://storage.googleapis.com/bucket/filename.pdf",
  "filename": "filename.pdf",
  "size": 102400
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
- `400` — File upload failed
