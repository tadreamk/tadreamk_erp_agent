# GET /job-application/interview-calendar

Interview Calendar. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| from_date | string | Yes | Window start (YYYY-MM-DD). |
| to_date | string | Yes | Window end (YYYY-MM-DD). |

**Response:**
```json
{
  "items": [
    {
      "workflow_id": "uuid",
      "candidate_name": "string",
      "position_title": "string",
      "interview_schedule_final": "string",
      "status": "string"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
