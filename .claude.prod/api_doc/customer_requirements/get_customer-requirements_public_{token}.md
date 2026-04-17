# GET /customer-requirements/public/{token}

Public bootstrap payload for the share-link editor page. **No authentication** — anyone with the token can call this.

Rate-limited to 60 requests per minute per client IP.

**Path parameter:** `token` — the 12-character share token.

**Response:**
```json
{
  "id": "uuid",
  "share_token": "abcdef123456",
  "title": "Example Requirement",
  "latest_yjs_state_b64": "<base64 Yjs encoded state or null>"
}
```

`latest_yjs_state_b64` is `null` for a brand-new requirement that has not been snapshotted yet.

**Errors:**
- `404` — token unknown, requirement soft-deleted, or `share_mode = "disabled"`
- `429` — IP rate limit exceeded
