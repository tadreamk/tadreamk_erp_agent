# GET /job-applications-workflow/staff-users


List usernames that have `job-applications` whitelist access. Used for @mention dropdowns in internal notes.

**Access:** Whitelist (`job-applications`)

**Response:**
```json
{
  "users": ["recruiter1", "tech_lead", "hr_manager"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Whitelist access required
