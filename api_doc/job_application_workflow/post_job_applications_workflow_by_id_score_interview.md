# POST /job-applications-workflow/{workflow_id}/score-interview


Score a completed interview. Optionally attach a feedback note.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| score | int | Yes | Score from 1 to 5 |
| note_content | string | No | Optional feedback note (min length: 1 if provided) |

**Request Example:**
```json
{
  "score": 5,
  "note_content": "Excellent communication skills. Strong technical depth. Recommended for hire."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Interview scored: 5/5",
  "new_status": "interview_confirmed"
}
```

Note: Scoring the interview does **not** change the workflow status. The status remains at its current value.

**Side Effects:**
- Records the score, scorer username, and timestamp on the workflow
- Creates a workflow note if `note_content` is provided

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
- `422` — Validation error (score out of range)
