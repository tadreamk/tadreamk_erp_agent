# GET /job-applications-workflow/stats


Get workflow counts grouped by status.

**Access:** Whitelist (`job-applications`)

**Response:**
```json
{
  "submitted": 10,
  "exercise_assigned": 5,
  "exercise_submitted": 3,
  "exercise_scored": 2,
  "interview_proposed": 4,
  "interview_negotiating": 1,
  "interview_confirmed": 2,
  "interview_finished": 1,
  "accepted": 8,
  "rejected": 12,
  "archived": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Whitelist access required
