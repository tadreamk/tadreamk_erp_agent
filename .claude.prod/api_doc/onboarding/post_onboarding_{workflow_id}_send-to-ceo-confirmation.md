# POST /onboarding/{workflow_id}/send-to-ceo-confirmation

HR sends documents to CEO for confirmation, transitioning status from `template_selection` to `ceo_confirmation`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK`
```json
{
  "message": "Sent to CEO for confirmation",
  "status": "ceo_confirmation"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
