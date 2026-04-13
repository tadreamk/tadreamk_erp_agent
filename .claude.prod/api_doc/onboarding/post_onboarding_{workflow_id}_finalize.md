# POST /onboarding/{workflow_id}/finalize

CEO finalizes the onboarding workflow, transitioning status from `ceo_signature` to `completed`. Validates all CEO signatures are present before finalizing.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access.

**Response:** `200 OK`
```json
{
  "message": "Onboarding finalized and contract sent",
  "status": "completed"
}
```

**Errors:**
- `400` — CEO signature required on one or more documents
- `401` — Not authenticated
- `403` — Only CEO can finalize
- `404` — Workflow not found
