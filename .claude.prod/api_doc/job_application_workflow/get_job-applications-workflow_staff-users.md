# GET /job-applications-workflow/staff-users

List usernames with `job-applications` whitelist access (used for mention dropdowns in notes). Requires `job-applications` whitelist.

**Response:**
```json
{
  "users": ["alice", "bob", "charlie"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
