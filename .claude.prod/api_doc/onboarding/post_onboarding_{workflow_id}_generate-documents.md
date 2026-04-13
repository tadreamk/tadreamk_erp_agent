# POST /onboarding/{workflow_id}/generate-documents

Validates that documents have been added to the workflow. Workflow must be in `template_selection` status and have at least one document.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK`
```json
{
  "message": "Documents generated. 3 document(s) ready for HR input.",
  "status": "template_selection"
}
```

**Errors:**
- `400` — Can only generate from template_selection status
- `400` — No documents added to workflow
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
