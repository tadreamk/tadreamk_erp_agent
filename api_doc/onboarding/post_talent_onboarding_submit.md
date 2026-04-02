# POST /talent/onboarding/submit

Talent confirms all documents are signed and submits for HR review. Transitions status from `talent_input` to `hr_review`. All documents must be signed or have an uploaded PDF. Generates PDFs for eligible documents before submitting.

**Auth:** Requires authentication. Must be the talent on an active `talent_input` workflow.

**Response:** `200 OK`
```json
{
  "message": "All documents signed and submitted. Awaiting HR review.",
  "status": "hr_review",
  "talent_submitted_at": "2024-01-01T00:00:00+00:00"
}
```

**Errors:**
- `400` — All docs must be signed or have PDF. N incomplete.
- `401` — Not authenticated
- `404` — No active onboarding found
