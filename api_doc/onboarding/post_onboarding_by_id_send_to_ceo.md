# POST /onboarding/{workflow_id}/send-to-ceo


HR sends the workflow to CEO for final signature. Requires the talent to have submitted first (`talent_submitted_at` must be set). Sets `sent_to_ceo_at` timestamp. Sends notification to the CEO.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Access:** HR only (whitelist required).

**Response:**
```json
{
  "message": "Sent to CEO (ceo.user)",
  "status": "input",
  "sent_to_ceo_at": "2026-03-10T12:00:00+00:00"
}
```

**Errors:**
- `400` — Workflow not in `input` status; talent must submit first
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Workflow not found
