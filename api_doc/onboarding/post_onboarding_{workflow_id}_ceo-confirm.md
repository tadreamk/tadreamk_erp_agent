# POST /onboarding/{workflow_id}/ceo-confirm

CEO confirms onboarding documents, transitioning status from `ceo_confirmation` to `talent_input`. Requires CEO role on the workflow.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access.

**Response:** `200 OK`
```json
{
  "message": "CEO confirmed onboarding documents",
  "status": "talent_input"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only CEO can confirm documents
- `404` — Workflow not found
