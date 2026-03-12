# POST /onboarding/{workflow_id}/reopen


Reopen a cancelled workflow. Transitions from `cancelled` back to `template_selection`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Workflow reopened",
  "status": "template_selection"
}
```

**Errors:**
- `400` — Workflow is not in `cancelled` status
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
