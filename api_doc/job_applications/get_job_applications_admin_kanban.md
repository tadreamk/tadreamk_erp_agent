# GET /job-applications/admin/kanban


Get applications grouped by status columns for a Kanban board view. Optionally filtered by job post.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| job_post_id | string (UUID) | No | null | Filter by job post ID |

**Response (200):**
```json
{
  "columns": {
    "submitted": {
      "id": "submitted",
      "title": "Submitted",
      "count": 5,
      "applications": [ { "...": "..." } ]
    },
    "exercise_assigned": {
      "id": "exercise_assigned",
      "title": "Exercise Assigned",
      "count": 3,
      "applications": [ { "...": "..." } ]
    }
  },
  "column_order": [
    "submitted",
    "exercise_assigned",
    "exercise_submitted",
    "exercise_scored",
    "interview_proposed",
    "interview_negotiating",
    "interview_confirmed",
    "interview_finished",
    "accepted",
    "rejected"
  ]
}
```

If the user lacks whitelist access, returns `{"columns": {}, "column_order": []}`.

**Error Codes:**
| Code | Detail |
|------|--------|
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
