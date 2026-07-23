# GET /job-application/staff-users

List Staff Users. Requires authentication.

**Response:**
```json
{
  "users": [
    "string"
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
