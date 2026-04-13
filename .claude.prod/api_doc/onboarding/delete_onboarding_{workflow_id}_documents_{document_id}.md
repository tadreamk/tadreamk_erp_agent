# DELETE /onboarding/{workflow_id}/documents/{document_id}

Remove a document from a workflow. Workflow must be in `template_selection` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |
| document_id | UUID | The document's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Response:** `200 OK`
```json
{
  "message": "Document removed from workflow"
}
```

**Errors:**
- `400` — Can only remove documents in template_selection status
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow or document not found
