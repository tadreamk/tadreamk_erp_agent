# GET /onboarding/{workflow_id}

Get an onboarding workflow with its documents. Accessible by HR, talent, and CEO. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Response:** Workflow object with documents
```json
{
  "id": "uuid",
  "talent_email": "talent@example.com",
  "talent_username": "string",
  "hr_username": "string",
  "ceo_username": "string",
  "status": "pending",
  "documents": [],
  "user_role": "hr",
  "is_active": true,
  "talent_submitted_at": "2024-01-02T00:00:00",
  "sent_to_ceo_at": "2024-01-03T00:00:00",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-03T00:00:00"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this workflow
- `404` — Workflow not found
