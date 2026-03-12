# POST /onboarding/{workflow_id}/finalize


CEO finalizes the onboarding and completes the workflow. Validates all CEO signatures are present, transitions to `complete`, creates leave entitlements, and sends completion notification and email (if email setting enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Access:** CEO only.

**Preconditions:**
- Workflow must be in `input` status
- `sent_to_ceo_at` must be set (HR must have sent to CEO first)
- All documents requiring CEO signature must be signed

**Response:**
```json
{
  "message": "Onboarding finalized and contract sent",
  "status": "complete"
}
```

**Errors:**
- `400` — Workflow not in `input` status; not sent to CEO yet; CEO signature required on one or more documents
- `401` — Not authenticated
- `403` — Only CEO can finalize; no access to workflow
- `404` — Onboarding workflow not found

---

## 29. Onboarding Notes

Internal staff-only notes on onboarding workflows. Notes are visible to HR and CEO but **not** to Talent. Only the note author can update or delete their own notes. WebSocket broadcast is sent on every note change.
