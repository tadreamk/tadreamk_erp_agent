# GET /job-applications/admin/stats

Get application statistics grouped by status. Requires `job-applications` whitelist. Returns zeros if no access.

**Response:**
```json
{
  "total": 100,
  "submitted": 20,
  "exercise_assigned": 15,
  "exercise_submitted": 10,
  "exercise_scored": 8,
  "interview_proposed": 6,
  "interview_confirmed": 5,
  "interview_finished": 4,
  "accepted": 2,
  "rejected": 30
}
```

**Errors:**
- `401` — Not authenticated
