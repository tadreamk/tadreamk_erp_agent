# POST /articles/image-storage


Upload an image to GCP storage. Returns the public URL.

**Auth:** Requires authentication (no whitelist needed).

**Request:** Multipart form upload with `file` field.

**Constraints:**
- Allowed types: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
- Max size: 2 MB

**Response:**
```json
{
  "url": "https://storage.googleapis.com/.../image.png",
  "filename": "original-filename.png",
  "size": 102400
}
```

**Errors:**
- `400` — Invalid file type or file too large
- `500` — Upload failed
