# DELETE /onboarding/{workflow_id}

Soft delete an onboarding workflow. Requires `onboarding` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Response:**
```json
{
  "message": "Onboarding workflow deleted"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
