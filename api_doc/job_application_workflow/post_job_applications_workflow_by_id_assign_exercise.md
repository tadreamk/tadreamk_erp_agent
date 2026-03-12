# POST /job-applications-workflow/{workflow_id}/assign-exercise


Assign an exercise to a candidate's workflow. Sends an email notification to the candidate with a link to the exercise.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_id | string (UUID) | Yes | Exercise UUID to assign |

**Request Example:**
```json
{
  "exercise_id": "uuid-of-exercise"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Exercise assigned successfully",
  "new_status": "exercise_assigned"
}
```

**Side Effects:**
- Sets status to `exercise_assigned`
- Sends email to the candidate with exercise instructions and workflow link

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
