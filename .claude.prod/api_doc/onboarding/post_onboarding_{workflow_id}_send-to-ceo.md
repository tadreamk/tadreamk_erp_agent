# POST /onboarding/{workflow_id}/send-to-ceo

HR sends documents to CEO for final signature, transitioning status from `hr_review` to `ceo_signature`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK`
```json
{
  "message": "Sent to CEO (ceo_username)",
  "status": "ceo_signature",
  "sent_to_ceo_at": "2024-01-01T00:00:00+00:00"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
