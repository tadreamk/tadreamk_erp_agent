# POST /job-applications-workflow/{workflow_id}/interview-propose


Propose interview time slots to the candidate. Sends an email to the candidate with the proposed slots.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| time_slots | string[] | Yes | List of proposed time slots (1-5 items) |
| interview_url | string | No | Meeting URL for the interview |

**Request Example:**
```json
{
  "time_slots": [
    "2026-02-01 10:00 (GMT+7)",
    "2026-02-02 14:00 (GMT+7)",
    "2026-02-03 09:00 (GMT+7)"
  ],
  "interview_url": "https://meet.google.com/abc-defg-hij"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Interview slots proposed",
  "status": "interview_proposed",
  "interview_schedule_admin": [
    "2026-02-01 10:00 (GMT+7)",
    "2026-02-02 14:00 (GMT+7)",
    "2026-02-03 09:00 (GMT+7)"
  ],
  "interview_schedule_final": null,
  "interview_url": "https://meet.google.com/abc-defg-hij"
}
```

**Side Effects:**
- Sets status to `interview_proposed`
- Sends email to the candidate listing the proposed time slots

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
- `422` — Validation error (empty time_slots or more than 5)
