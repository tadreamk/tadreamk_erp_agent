# POST /job-applications-workflow/{workflow_id}/score-exercise

Score an exercise submission. Optionally creates a feedback note.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| score | integer | Yes | Score from 1-5 |
| note_content | string | No | Optional feedback note content |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Exercise scored: 4/5",
  "status": "exercise_scored"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Not on job-applications whitelist
- `404` — Workflow not found
