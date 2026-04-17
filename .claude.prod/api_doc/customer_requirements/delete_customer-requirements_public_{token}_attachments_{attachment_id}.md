# DELETE /customer-requirements/public/{token}/attachments/{attachment_id}

Delete one attachment row from a public Customer Requirement. **No authentication.** Rate-limited.

The underlying GCS object is **not** removed — only the database row. (A cleanup pass is a future enhancement.)

**Path parameters:**
- `token` — the 12-character share token.
- `attachment_id` — the UUID of the attachment to delete.

**Response:** `204 No Content`.

**Errors:**
- `400` — attachment_id is not a valid UUID
- `404` — token unknown / disabled / soft-deleted, or attachment doesn't belong to this requirement
- `429` — IP rate limit exceeded
