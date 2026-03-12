# POST /onboarding/{workflow_id}/send-to-ceo-confirmation


Send documents to CEO for review and confirmation. Transitions workflow from `template_selection` to `pending_ceo_confirmation`. Sends in-app notification to the assigned CEO.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Sent to CEO for confirmation",
  "status": "pending_ceo_confirmation"
}
```

**Errors:**
- `400` — Workflow not in `template_selection` status; no documents in workflow
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
