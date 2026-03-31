# GET /timesheet-workflow/employees

Get list of hourly employees with their contract info. Requires `timesheet` whitelist.

**Response:**
```json
[
  {
    "username": "john_doe",
    "full_name": "Doe, John",
    "hourly_rate": 25.00,
    "department": "Engineering",
    "position": "Developer",
    "manager_username": "manager_user"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No timesheet whitelist access
