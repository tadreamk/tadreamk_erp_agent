# GET /job-application/my-stats

My Workflow Stats. Requires authentication.

**Response:**
```json
{
  "total": 0,
  "bookmarked": 0,
  "submitted": 0,
  "exercise_assigned": 0,
  "exercise_submitted": 0,
  "exercise_scored": 0,
  "interview_proposed": 0,
  "interview_confirmed": 0,
  "interview_finished": 0,
  "accepted": 0,
  "rejected": 0,
  "archived": 0
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
