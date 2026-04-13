# POST /job-applications-workflow/{workflow_id}/interview-accept

Accept an interview time slot. Talent only — must be the workflow owner.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires authentication. Must be the candidate on the workflow.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| selected_slot | string | Yes | Selected time slot from proposed options |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Interview confirmed for 2024-01-15 10:00",
  "status": "interview_confirmed",
  "interview_schedule_admin": ["2024-01-15 10:00", "2024-01-16 14:00"],
  "interview_schedule_final": "2024-01-15 10:00",
  "interview_url": "https://meet.google.com/..."
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — You can only accept interview slots for your own application
- `404` — Workflow not found
