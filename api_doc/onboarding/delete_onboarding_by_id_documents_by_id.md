# DELETE /onboarding/{workflow_id}/documents/{document_id}


Remove a document from a workflow (HR only). Only allowed in `template_selection` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |
| document_id | UUID | Document ID |

**Response:**
```json
{
  "message": "Document removed from workflow"
}
```

**Errors:**
- `400` — Workflow not in `template_selection` status
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow or document not found; document not in this workflow
