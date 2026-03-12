# POST /onboarding/{workflow_id}/ceo-confirm


CEO confirms the prepared documents. Transitions workflow from `pending_ceo_confirmation` to `input`. Sends notification to the assigned HR user.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Access:** CEO only (the CEO assigned to the workflow via `ceo_username`).

**Response:**
```json
{
  "message": "CEO confirmed onboarding documents",
  "status": "input"
}
```

**Errors:**
- `400` — Workflow not in `pending_ceo_confirmation` status
- `401` — Not authenticated
- `403` — Only CEO can confirm documents; no access to workflow
- `404` — Onboarding workflow not found
