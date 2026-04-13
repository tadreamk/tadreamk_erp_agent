# POST /articles/image-storage

Upload an image file to GCP image storage and get back a public URL. Requires authentication (no whitelist check).

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | Image file (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`). Max 2 MB. |

**Response:**
```json
{
  "url": "https://storage.googleapis.com/...",
  "filename": "original_filename.png",
  "size": 102400
}
```

**Errors:**
- `400` — Invalid file type or file too large (max 2 MB)
- `401` — Not authenticated
- `500` — GCP upload failure
