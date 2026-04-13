# GET /job-applications/admin/kanban

Get applications grouped by status for Kanban board display. Requires `job-applications` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | string | No | Filter by job post ID |

**Response:**
```json
{
  "columns": {
    "submitted": {
      "id": "submitted",
      "title": "Submitted",
      "count": 20,
      "applications": [ { "...application object..." } ]
    }
  },
  "column_order": ["submitted", "exercise_assigned", "exercise_submitted", "exercise_scored", "interview_proposed", "interview_confirmed", "interview_finished", "accepted", "rejected"]
}
```

**Errors:**
- `401` — Not authenticated
