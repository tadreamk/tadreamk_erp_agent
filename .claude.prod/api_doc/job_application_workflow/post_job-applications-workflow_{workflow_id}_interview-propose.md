# POST /job-applications-workflow/{workflow_id}/interview-propose

Propose interview time slots to the candidate. Sends an email with the proposed slots.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| time_slots | array[string] | Yes | 1-5 proposed time slots |
| interview_url | string | No | Meeting URL for the interview |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Interview slots proposed",
  "status": "interview_proposed",
  "interview_schedule_admin": ["2024-01-15 10:00", "2024-01-16 14:00"],
  "interview_schedule_final": null,
  "interview_url": "https://meet.google.com/..."
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Not on job-applications whitelist
- `404` — Workflow not found
