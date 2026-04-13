# GET /job-applications-workflow/my-stats

Get workflow statistics for the authenticated user. Requires authentication.

**Response:** Flat dict with `total` and per-status counts as top-level keys.
```json
{
  "total": 3,
  "new": 1,
  "interview": 1,
  "approved": 1
}
```

**Errors:**
- `401` — Not authenticated
