# GET /customer-requirements/public/{token}/attachments

List all attachments for a public Customer Requirement, newest first. **No authentication.** Rate-limited to 60 requests / minute / IP (shared budget with the other public endpoints).

**Path parameter:** `token` — the 12-character share token.

**Response:**
```json
[
  {
    "id": "uuid",
    "filename": "spec.pdf",
    "url": "https://storage.googleapis.com/.../spec.pdf",
    "content_type": "application/pdf",
    "size_bytes": 102400,
    "uploaded_at": "2026-04-16T16:20:00+00:00"
  }
]
```

**Errors:**
- `404` — token unknown, requirement soft-deleted, or `share_mode = "disabled"`
- `429` — IP rate limit exceeded
