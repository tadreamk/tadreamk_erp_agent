# POST /customer-requirements/public/{token}/attachments

Upload one file as a public attachment on a Customer Requirement. **No authentication.** Rate-limited.

**Request body:** `multipart/form-data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | file | Yes | One of the allowlisted extensions (see below). Max 2 MB. |

**Allowed extensions** (case-insensitive):

- Images: `.png` `.jpg` `.jpeg` `.gif` `.webp` (frontend auto-compresses to ≤ 900 KB before upload)
- Documents: `.pdf` `.docx` `.xlsx` `.pptx` `.txt` `.csv` `.json` `.md`
- Archives: `.zip`

Anything outside this list — including files with no extension — is rejected with 400.

**Response:** `CustomerRequirementAttachmentResponse` (see GET attachments for shape).

**Errors:**
- `400` — File too large (> 2 MB), or extension is not in the allowlist
- `404` — token unknown, soft-deleted, or `disabled`
- `429` — IP rate limit exceeded
- `500` — GCS upload failure
