# GET /admin/leave/stats

Get leave dashboard statistics. Requires `leave-management` whitelist.

**Response:**
```json
{
  "total_pending": 5,
  "total_approved": 50,
  "total_rejected": 10,
  "employees_on_leave_today": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
