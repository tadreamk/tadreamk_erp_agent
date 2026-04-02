# GET /job-applications-workflow/stats

Get workflow counts grouped by status. Requires `job-applications` whitelist.

**Response:** Flat dict with `total` and per-status counts as top-level keys.
```json
{
  "total": 100,
  "new": 10,
  "screening": 20,
  "interview": 15,
  "offer": 5,
  "approved": 30,
  "rejected": 15,
  "archived": 5
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
