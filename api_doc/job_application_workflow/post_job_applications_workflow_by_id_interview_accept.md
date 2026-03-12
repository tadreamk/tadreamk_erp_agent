# POST /job-applications-workflow/{workflow_id}/interview-accept


Accept one of the proposed interview time slots. Only the candidate who owns the workflow can accept.

**Access:** Authenticated (workflow owner only)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| selected_slot | string | Yes | The selected time slot from the proposed options |

**Request Example:**
```json
{
  "selected_slot": "2026-02-01 10:00 (GMT+7)"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Interview confirmed for 2026-02-01 10:00 (GMT+7)",
  "status": "interview_confirmed",
  "interview_schedule_admin": [
    "2026-02-01 10:00 (GMT+7)",
    "2026-02-02 14:00 (GMT+7)",
    "2026-02-03 09:00 (GMT+7)"
  ],
  "interview_schedule_final": "2026-02-01 10:00 (GMT+7)",
  "interview_url": "https://meet.google.com/abc-defg-hij"
}
```

**Side Effects:**
- Sets status to `interview_confirmed`
- Sends in-app notification to users with the `head_of_recruitment` role

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Not the workflow owner
- `404` — Workflow not found
