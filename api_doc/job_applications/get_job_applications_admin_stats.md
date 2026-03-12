# GET /job-applications/admin/stats


Get application statistics grouped by status. Returns counts for each pipeline stage.

**Response (200):**
```json
{
  "total": 42,
  "submitted": 10,
  "exercise_assigned": 5,
  "exercise_submitted": 3,
  "exercise_scored": 4,
  "interview_proposed": 2,
  "interview_negotiating": 1,
  "interview_confirmed": 3,
  "interview_finished": 2,
  "accepted": 8,
  "rejected": 4
}
```

If the user lacks whitelist access, all values return `0`.

**Error Codes:**
| Code | Detail |
|------|--------|
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
