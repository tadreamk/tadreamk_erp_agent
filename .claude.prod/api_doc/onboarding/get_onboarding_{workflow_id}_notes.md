# GET /onboarding/{workflow_id}/notes

List internal notes for an onboarding workflow. Staff only (HR or CEO) — not visible to talent.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist or CEO owner access. Talent is denied.

**Response:** `200 OK`
```json
{
  "notes": [
    {
      "id": "uuid",
      "workflow_id": "uuid",
      "username": "hr_user",
      "content": "Note text",
      "created_at": "2024-01-01T00:00:00+00:00",
      "updated_at": "2024-01-01T00:00:00+00:00"
    }
  ],
  "total": 1
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent
- `404` — Workflow not found
