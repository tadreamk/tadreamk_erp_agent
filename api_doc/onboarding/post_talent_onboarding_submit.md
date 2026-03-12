# POST /talent/onboarding/submit


Talent submits all documents, confirming everything is signed. All documents must be either signed (locked) or have an uploaded PDF. Sets `talent_submitted_at` timestamp. Sends notification to HR and confirmation email to talent (if email setting enabled).

**Preconditions:**
- At least one active workflow in `input` status must exist for the authenticated user
- Documents must not have been already submitted (`talent_submitted_at` must be null)
- All documents must be signed or have an uploaded PDF

**Response:**
```json
{
  "message": "All documents signed and submitted. Awaiting HR review.",
  "status": "input",
  "talent_submitted_at": "2026-03-07T09:00:00+00:00"
}
```

**Errors:**
- `400` — Documents already submitted; incomplete documents remain (not all signed or with PDF)
- `401` — Not authenticated
- `404` — No active onboarding found
