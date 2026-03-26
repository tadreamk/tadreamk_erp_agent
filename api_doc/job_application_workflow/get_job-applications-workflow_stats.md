# GET /job-applications-workflow/stats

Get workflow counts grouped by status. Requires `job-applications` whitelist.

**Response:**
```json
{
  "total": 100,
  "by_status": {
    "new": 10,
    "screening": 20,
    "interview": 15,
    "offer": 5,
    "approved": 30,
    "rejected": 15,
    "archived": 5
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
