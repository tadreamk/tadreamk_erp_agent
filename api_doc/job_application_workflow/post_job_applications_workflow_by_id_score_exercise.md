# POST /job-applications-workflow/{workflow_id}/score-exercise


Score an exercise submission. Optionally attach a feedback note.

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
  "score": 4,
  "note_content": "Clean code structure. Good use of design patterns. Minor issues with error handling."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Exercise scored: 4/5",
  "new_status": "exercise_scored"
}
```

**Side Effects:**
- Sets status to `exercise_scored`
- Creates a workflow note if `note_content` is provided
- Sends in-app notification to users with the `head_of_recruitment` role

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
- `422` — Validation error (score out of range)
