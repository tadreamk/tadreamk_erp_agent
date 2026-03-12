# GET /job-applications-workflow/my-stats


Get workflow statistics for the authenticated user (talent/candidate view).

**Access:** Authenticated (any user)

**Response:**
```json
{
  "submitted": 1,
  "exercise_assigned": 0,
  "interview_confirmed": 1,
  "accepted": 0
}
```

**Errors:**
- `401` — Not authenticated
