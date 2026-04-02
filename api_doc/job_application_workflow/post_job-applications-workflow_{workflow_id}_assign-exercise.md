# POST /job-applications-workflow/{workflow_id}/assign-exercise

Assign an exercise to a candidate's workflow. Sends an email notification to the candidate.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `job-applications` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_id | string | Yes | Exercise UUID to assign |

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Exercise assigned successfully",
  "status": "exercise_sent"
}
```

**Errors:**
- `400` — Invalid workflow_id format
- `401` — Not authenticated
- `403` — Not on job-applications whitelist
- `404` — Workflow not found
