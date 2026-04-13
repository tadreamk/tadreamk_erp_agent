# POST /onboarding/{workflow_id}/return-to-talent

HR returns documents to talent for further changes.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK`
```json
{
  "message": "Documents returned to talent",
  "status": "talent_input",
  "talent_submitted_at": null
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
