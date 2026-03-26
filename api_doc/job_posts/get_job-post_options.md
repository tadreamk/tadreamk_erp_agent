# GET /job-post/options

Get available form options (departments and job types) for creating/editing job posts. Requires `job_post` whitelist.

**Response:**
```json
{
  "departments": [
    { "value": "Engineering", "label": "Engineering" }
  ],
  "job_types": [
    { "value": "full_time", "label": "Full Time" }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job_post whitelist access
