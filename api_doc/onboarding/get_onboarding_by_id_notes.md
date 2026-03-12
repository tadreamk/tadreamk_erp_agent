# GET /onboarding/{workflow_id}/notes


List all notes for a workflow. Ordered by creation time.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string (UUID) | Onboarding workflow ID |

**Access:** HR or CEO only. Talent is blocked.

**Response:**
```json
{
  "notes": [
    {
      "id": "uuid",
      "workflow_id": "uuid",
      "username": "hr.admin",
      "content": "Called the candidate to confirm start date.",
      "created_at": "2026-03-05T09:00:00+00:00",
      "updated_at": "2026-03-05T09:00:00+00:00"
    }
  ],
  "total": 1
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent; no access to workflow
- `404` — Onboarding workflow not found
