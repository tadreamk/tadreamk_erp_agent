# GET /job-applications-workflow/my-stats

Get workflow statistics for the authenticated user. Requires authentication.

**Response:**
```json
{
  "total": 3,
  "by_status": {
    "new": 1,
    "interview": 1,
    "approved": 1
  }
}
```

**Errors:**
- `401` — Not authenticated
