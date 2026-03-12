# POST /onboarding/{workflow_id}/generate-documents


Generate documents from selected templates. Validates that documents have been added. Workflow stays in `template_selection` status for continued HR input.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Documents generated. 3 document(s) ready for HR input.",
  "status": "template_selection"
}
```

**Errors:**
- `400` — Workflow not in `template_selection` status; no documents added to workflow
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
